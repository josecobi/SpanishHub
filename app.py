import os
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required
from datetime import datetime
from markupsafe import escape

app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def index():
    return render_template('/index.html')

@app.route("/dragndrop")
def dragndrop():
    
    return render_template("dragndrop.html")

if __name__ == "__main__":
    app.run(debug=True)

