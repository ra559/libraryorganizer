from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

#connection to database
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_DB'] = 'liborg'
mysql = MySQL(app)


@app.route('/')
def login():
    return render_template('login.html')

#login page route
@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
       user_email =  request.form['user_email']
       user_passwd =  request.form['user_passwd']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (user_email, user_passwd VALUES (%s %s)", (user_email,user_passwd))
    mysql.connection.commit()
    return redirect(url_for('login.html'))

#signup page route
@app.route('/insert_2', methods = ['POST'])
def insert():
    if request.method == 'POST':
       user_email =  request.form['user_email']
       user_passwd =  request.form['user_passwd']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (user_email, user_passwd VALUES (%s %s)", (user_email,user_passwd))
    mysql.connection.commit()
    return redirect(url_for('signup.html'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
