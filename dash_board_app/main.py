from typing import Sequence
from flask import Flask, render_template, request, redirect, url_for, session,flash, jsonify, json
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re



app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = '1a2b3c4d5e'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'mysqldb'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'test'
app.config['MYSQL_DB'] = 'demo'

# Intialize MySQL
mysql = MySQL(app)

# http://localhost:5000/pythonlogin/ - this will be the login page, we need to use both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
# Output message if something goes wrong...
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
                # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            session['role'] = account['role']
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            flash("Incorrect username/password!", "danger")
    return render_template('auth/login.html',title="Login")



# http://localhost:5000/pythinlogin/register 
# This will be the registration page, we need to use both GET and POST requests
@app.route('/pythonlogin/register', methods=['GET', 'POST'])
def register():
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
                # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('SELECT * FROM accounts WHERE username = %s', (username))
        cursor.execute( "SELECT * FROM accounts WHERE username LIKE %s", [username] )
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            flash("Account already exists!", "danger")
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash("Invalid email address!", "danger")
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash("Username must contain only characters and numbers!", "danger")
        elif not username or not password or not email:
            flash("Incorrect username/password!", "danger")
        else:
        # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s, default)', (username,password, email))
            mysql.connection.commit()
            flash("You have successfully registered!", "success")
            return redirect(url_for('login'))

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        flash("Please fill out the form!", "danger")
    # Show registration form with message (if any)
    return render_template('auth/register.html',title="Register")

# http://localhost:5000/pythinlogin/home 
# This will be the home page, only accessible for loggedin users

@app.route('/pythonlogin/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        if session['role'] != 1:
            return render_template('home/home.html', username=session['username'],role=session['role'])
        else:
            # Fetch all user account info by MySQL
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            # cursor.execute('SELECT * FROM accounts WHERE username = %s', (username))
            cursor.execute( "SELECT * FROM accounts")
            accounts = cursor.fetchall()
            return render_template('home/home.html', accounts=accounts, username=session['username'],role=session['role'])
            
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))    


# http://localhost:5000/pythinlogin/profile - this will be the profile page, only accessible for loggedin users
@app.route('/pythonlogin/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('auth/profile.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login')) 

# http://localhost:5000/python/logout - this will be the logout page
@app.route('/pythonlogin/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))

# Admin page
@app.route('/select', methods=['GET', 'POST'])
def select():   
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST': 
        id = request.form['id']
        cursor.execute("SELECT * FROM accounts WHERE id = %s", [id])
        rs = cursor.fetchone()
        employee_dict = {
                    'id': rs['id'],
                    'username': rs['username'],
                    'email': rs['email'],
                    'role': rs['role'],
                    'password': rs['password']}
        return json.dumps(employee_dict)

# Add new record
@app.route('/insert', methods=['GET', 'POST'])
def insert():   
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        role = request.form['role']
        if role == '':
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s, default)', (username, password, email))
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s, %s)', (username, password, email, role))

        mysql.connection.commit()
        cursor.close()
    return jsonify('success')

# Update record
@app.route('/update', methods=['GET', 'POST'])
def update():   
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        role = request.form['role']
        id = request.form['id']
        cursor.execute('UPDATE accounts SET username=%s, password=%s, email=%s, role=%s WHERE id=%s', (username, password, email, role, id))
        mysql.connection.commit()
        cursor.close()
    return jsonify('success')

# Del record
@app.route('/delete', methods=['GET', 'POST'])
def delete():   
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST': 
        id = request.form['id']
        cursor.execute('DELETE FROM accounts WHERE id=%s', (id,))
        mysql.connection.commit()
        cursor.close()
    return jsonify('success')

if __name__ =='__main__':
	app.run(debug=True, host="0.0.0.0")
