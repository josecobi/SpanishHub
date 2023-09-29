import os
from flask import Flask, render_template, g, jsonify, abort
from flask_session import Session
import sqlite3

# Configure application
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.static_folder = 'static'

# Configure session (filesystem)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def connect_db():
    sql = sqlite3.connect('questions_answers.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
        return g.sqlite3_db
    
# Make sure that the responses from the application are not cached in order to have more up to date data displayed to the user.   
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template('/index.html')

@app.route("/verbsMultChoiceQuiz")
def dragndrop():
    return render_template("/verbsMultChoiceQuiz.html")

@app.route("/tenses/<tense>")
def get_tense(tense):
    conn = connect_db()
    cursor = conn.cursor()
    if tense == "present":
        cursor.execute('SELECT * FROM present_tense')
        questions = [dict(row) for row in cursor.fetchall()]
        cursor.execute('SELECT * FROM choices_present')
        choices = [dict(row) for row in cursor.fetchall()]

        # Handle the case where the database query returned no results
        if not questions or not choices:           
            abort(404)
    if tense == "present_stem_changing":
        cursor.execute('SELECT * FROM present_tense_stem_changing')
        questions = [dict(row) for row in cursor.fetchall()]
        cursor.execute('SELECT * FROM choices_present_stem_changing')
        choices = [dict(row) for row in cursor.fetchall()]

        if not questions or not choices:
            # Handle the case where the database query returned no results
            abort(404)

    if tense == "preterit":
        cursor.execute('SELECT * FROM preterit_tense')
        questions = [dict(row) for row in cursor.fetchall()]
        cursor.execute('SELECT * FROM choices_preterit')
        choices = [dict(row) for row in cursor.fetchall()]

        # Handle the case where the database query returned no results
        if not questions or not choices:           
            abort(404)

    return jsonify({'questions': questions, 'choices': choices})
    
    
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

if __name__ == "__main__":
    app.run(debug=True)

