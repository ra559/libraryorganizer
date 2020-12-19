from flask import Flask, url_for, render_template, request, url_for, redirect, session, abort, flash
from random import randint
from flask_wtf import FlaskForm
from typing import List, Dict
import mysql.connector
import simplejson as json
from wtforms import StringField, PasswordField

import random
import string

def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

chars = string.ascii_letters + string.punctuation
size = 12

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = random_string_generator(size, chars)


@app.route("/", methods=["POST", "GET"])
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST"])
def login():
    return render_template("login.html")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    return render_template("signup.html")


@app.route("/book", methods=["POST", "GET"])
def book():
    return render_template("book.html")


@app.route("/forgot", methods=["POST", "GET"])
def forgot():
    return render_template("forgot.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    return render_template("user.html")


@app.route("/booklist", methods=["POST", "GET"])
def booklist():
    return render_template("booklist.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
