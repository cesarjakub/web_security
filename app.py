from flask import Flask, render_template, session, request, redirect, url_for, flash, abort
from dotenv import load_dotenv
from flask_mysqldb import MySQL
import os
import hashlib

load_dotenv()

app = Flask(__name__)

mysql = MySQL(app)

app.secret_key = os.getenv('TOKEN')

app.config['MYSQL_DB'] = os.getenv('DB_NAME')
app.config['MYSQL_HOST'] = os.getenv('DB_HOST')
app.config['MYSQL_USER'] = os.getenv('DB_USER')



@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["pass"]
        
        hash_pass = hash_password(password)
        print(hash_pass)

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()

        if user and check_password(password, user[3]) and check_email(email, user[2]):
            session["user"] = user
            return redirect(url_for("index"))
        
        flash("Password or email is incorrect", "warning")
        return render_template("login.html")
    
    return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        user_name = request.form["name"]
        email = request.form["email"]
        password = request.form["pass"]
        password_rept = request.form["passrept"]

        password_hash = hash_password(password)
        password_rept_hash = hash_password(password_rept)

        if password_hash == password_rept_hash:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO users (name, email, password) VALUES(%s, %s, %s)", (user_name, email, password_hash))
            mysql.connection.commit()
            cursor.close()
            return redirect(url_for("login"))
        else:
            flash('Passwords do not match. Please try again.', 'warning')
            return render_template("register.html")

    return render_template("register.html")


@app.route("/")
def index():
    if "user" in session:
        return render_template("index.html")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


def hash_password(password):
    salt = "salted password"
    password_with_salt = password + salt
    hashed_password = hashlib.sha256(password_with_salt.encode()).hexdigest()
    return hashed_password

def check_password(user_pass, db_pass):
    hash_user_pass = hash_password(user_pass)
    return hash_user_pass == db_pass

def check_email(user_email, db_email):
    return user_email == db_email


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)