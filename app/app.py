from typing import List, Dict
import mysql.connector
import simplejson as json
from flask import Flask, Response

app = Flask(__name__)


def liborg() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'liborg'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT * FROM books AND users')
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result

#App routes
@app.route('/')
def index() -> str:
    js = json.dumps(liborg())
    resp = Response(js, status=200, mimetype='application/json')
    return resp


@app.route("/", methods=["POST", "GET"])
def home():
    return render_template('index.html')

@app.route("/login", methods=["POST"])
def login():
    return render_template("login.html")

@app.route("/signup", methods=["POST"])
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