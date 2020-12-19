from flask import Flask, render_template
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my key'


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/book")
def book():
    return render_template("book.html")


@app.route("/forgot")
def forgot():
    return render_template("forgot.html")


@app.route("/user")
def user():
    return render_template("user.html")


@app.route("/booklist")
def booklist():
    return render_template("booklist.html")

@app.rout("/profile")
def profile():
    return render_template("profile.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
