from flask import Flask, render_template
from dotenv import load_dotenv
from flask_mysqldb import MySQL
import os

load_dotenv()

app = Flask(__name__)

mysql = MySQL(app)

app.config['MYSQL_DB'] = os.getenv('DB_NAME')
app.config['MYSQL_HOST'] = os.getenv('DB_HOST')
app.config['MYSQL_USER'] = os.getenv('DB_USER')



@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)