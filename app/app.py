from typing import List, Dict
from flask import Flask, request, Response, redirect, url_for, session
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from authlib.integrations.flask_client import OAuth
import os

from auth_decorator import login_required


from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key =os.getenv("APP_SECRET_KEY")
mysql = MySQL(cursorclass=DictCursor)

#OAuth
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='90827938468-2nabe3i97f9p51m2hi8g5r2q70fph8a2.apps.googleusercontent.com',
    client_secret='V-R0a4HVGiYZkPFAvE70T1Z-',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    access_params=None,
    authorize_base_url='https://googleapis.com/oauth2/vi/',
    api_base_url='https://googleapis.com/oauth2/vi/',
    client_kwargs={'scope': 'openid email profile'},
)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'liborg'
mysql.init_app(app)


@app.route('/')
@login_required
def index():
    email = dict(session)['email']
    return f'Hello, you are logge in as {email}!'


@app.route('/login')
def login():
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # create the google oauth client
    token = google.authorize_access_token()  # Access token from google (needed to get user info)
    resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    session['profile'] = user_info
    session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
    return redirect('/')


@app.route('/list', methods=['GET'])
def list():
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM books')
    result = cursor.fetchall()
    return render_template('list.html', books=result)


# called by regristration page to register user



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

@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
