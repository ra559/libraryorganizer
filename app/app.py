from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my key'


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        userDetails = request.form
        email = userDetails['email']
        password = userDetails['password']
    else:
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

@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
