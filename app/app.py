from flask import Flask, url_for, render_template, request, url_for, redirect, session

app = Flask(__name__, template_folder='templates')


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
