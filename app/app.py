from flask import Flask, url_for, render_template, request, url_for, redirect, session
from typing import List, Dict
import mysql.connector
import simplejson as json

app = Flask(__name__, template_folder='templates')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/book")
def book():
    return render_template("book.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/forgot")
def forgot():
    return render_template("forgot.html")


@app.route("/user")
def user():
    return render_template("user.html")


@app.route("/booklist")
def booklist():
    return render_template("booklist.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
