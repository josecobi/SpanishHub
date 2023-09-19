import os
import json
from flask import Flask, flash, redirect, render_template, g, request, session, url_for, jsonify, abort
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required
from datetime import datetime
from markupsafe import escape
import sqlite3

# Configure application

app = Flask(__name__)
app.secret_key = "#"
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


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    conn = connect_db()
    cursor = conn.cursor()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = cursor.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in. Session is a dictionary. "user_id" is a key and will be given the value of rows[0]["id"].
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    conn = connect_db()
    cursor = conn.cursor()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        existing_username = cursor.execute("SELECT username FROM users WHERE username = ?", username)
        # Check if the username provided exists in the database
        if not request.form.get("username"):
            return apology("Please use a valid username or password", 400)
        elif existing_username:
            return apology("This username already exist", 400)
        elif not request.form.get("password"):
            return apology("must provide password", 400)
        elif not request.form.get("confirmation"):
            return apology("must provide password confirmation", 400)
        elif (confirmation != password):
            return apology("Password and Password Confirmation must match", 400)
        hashed_password = generate_password_hash(password)
        cursor.execute("INSERT INTO users (username, hash) VALUES  (?, ?)", username, hashed_password)
        flash('You were successfully registered')
        return redirect("/login")

    else:
        return render_template("/register.html")


@app.route("/dragndrop")
def dragndrop():
    return render_template("/dragndrop.html")

@app.route("/tenses/<tense>")
def get_tense(tense):
    print(f"Accessed /tenses/{tense}")
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

    return jsonify({'questions': questions, 'choices': choices})
    
    
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

if __name__ == "__main__":
    app.run(debug=True)

