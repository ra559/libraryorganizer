from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

#connection to database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_DB'] = 'liborg'
mysql = MySQL(app)


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

#login page route
@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
       user_email =  request.form['user_email']
       user_passwd =  request.form['user_passwd']

    sql = "insert into `users` (`user_email`, `user_passwd`) values (%s, %s)"
    cursor = mysql.connection.cursor()
    cursor.execute(sql, (user_email,user_passwd))
    mysql.connection.commit()
    return redirect(url_for('login'))

#signup page route
@app.route('/insert_2', methods = ['POST'])
def insert_2():
    if request.method == 'POST':
       user_email =  request.form['user_email']
       user_passwd =  request.form['user_passwd']

    sql = "insert into `users` (`user_email`, `user_passwd`) values (%s, %s)"
    cursor = mysql.connection.cursor()
    cursor.execute(sql, (user_email,user_passwd))
    mysql.connection.commit()
    return redirect(url_for('signup'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
