from flask import Flask, url_for, render_template, request, url_for, redirect, session

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


if __name__ == '__main__':
    app.run(host='0.0.0.0')