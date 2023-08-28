import os
import json
from flask import Flask, flash, redirect, render_template, g, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required
from datetime import datetime
from markupsafe import escape
import sqlite3

app = Flask(__name__)
app.secret_key = "#"
app.static_folder = 'static'

def connect_db():
    sql = sqlite3.connect('questions_answers.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
        return g.sqlite3_db


@app.route("/")
def index():
    return render_template('/index.html')

@app.route("/dragndrop")
def dragndrop():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM present_tense')
    questions_present = cursor.fetchall()
    cursor.execute('SELECT * FROM choices_present')
    choices_present = cursor.fetchall()

    # Convert Row objects to dictionaries for JSON serialization
    questions_present_dict = [dict(row) for row in questions_present]
    choices_present_dict = [dict(row) for row in choices_present]

    return render_template("dragndrop.html", questions_present=json.dumps(questions_present_dict), choices_present=json.dumps(choices_present_dict))

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

if __name__ == "__main__":
    app.run(debug=True)

