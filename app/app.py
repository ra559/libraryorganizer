from flask import Flask, url_for, render_template, request, url_for, redirect, session
app = Flask(__name__)
app.secret_key='123'

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()