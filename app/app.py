from typing import List, Dict
from flask import Flask, request, Response, redirect, url_for
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
import requests
import re
app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'liborg'
mysql.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return render_template('user.html')
    else:
        return render_template('login.html')


@app.route('/list', methods=['GET'])
def list():
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM books')
    result = cursor.fetchall()
    return render_template('list.html', books=result)


# called by regristration page to register user
@app.route('/insert', methods=['POST', 'GET'])
def insert():
    if request.method == 'POST':
        user_email = request.form['user_email']
        user_passwd = request.form['user_password']
        cursor = mysql.get_db().cursor()
        cursor.execute("""INSERT INTO users (user_email,user_passwd) VALUES (%s,%s)""", (user_email, user_passwd))
        mysql.get_db().commit()
        return render_template('login.html')
    else:
        return render_template('register.html')


@app.route('/user', methods=["GET", "POST"])
def user():
    return render_template('user.html')


@app.route("/booksearch", methods=["POST", "GET"])
def booksearch():
    try:
        isbn1 = request.form['isbn']
        url = "http://openlibrary.org/search.json?q=" + isbn1
        res = requests.get(url)
        scone = res.json()
        lst = scone['docs']
        for item in lst:
            isbn = item['isbn']
            title = item['title']
            try:
                author = item['author_name']
            except KeyError:
                author = item['Anonymous']
            try:
                lang = item['language']
            except KeyError:
                lang = ['Eng']
            try:
                genre = item['subject']
            except KeyError:
                genre = ['Undefined']
            publisher = item['publisher']

        return render_template('list2.html', isbn=isbn[0], title=title, author=author[0], lang=lang[0],
                                   genre=genre[0],
                                   publisher=publisher[0])
    except:
        return render_template('booknotfound.html')


@app.route('/list2redirect', methods=["POST", 'GET'])
def list2redirect():
    return render_template('user.html')


@app.route('/bookadd', methods=['POST', 'GET'])
def bookadd():
    isbn2 = request.form['addbookisbn']
    url = "http://openlibrary.org/search.json?q=" + isbn2
    res = requests.get(url)
    scone = res.json()
    lst = scone['docs']
    for item in lst:
        isbn = item['isbn']
        title = item['title']
        try:
            author = item['author_name']
        except KeyError:
            author = item['Anonymous']
        try:
            lang = item['language']
        except KeyError:
            lang = ['Eng']
        try:
            genre = item['subject']
        except KeyError:
            genre = ['Undefined']
        publisher = item['publisher']

# validates the input for database eliminating all special chactacters.
# Example: Harry's will turn into Harrys
        isbn = re.sub('[^A-Za-z0-9 ]+', '', str(isbn[0]))
        title = re.sub('[^A-Za-z0-9 ]+', '', str(title))
        author = re.sub('[^A-Za-z0-9 ]+', '', str(author))
        lang = re.sub('[^A-Za-z0-9 ]+', '', str(lang[0]))
        genre = re.sub('[^A-Za-z0-9 ]+', '', str(genre[0]))
        publisher = re.sub('[^A-Za-z0-9 ]+', '', str(publisher[0]))

        cursor = mysql.get_db().cursor()
        cursor.execute("""INSERT INTO books (isbn,title,author,lang,genre,publisher) VALUES (%s,%s,%s,%s,%s,%s)""",
                       (isbn, title, author, lang, genre, publisher))
        mysql.get_db().commit()
        return render_template('user.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
