from flask import Flask, flash, render_template, request, session
import os
import sqlite3

app = Flask(__name__)

#Routing through decorators

#index decorator (log in/register route)
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('loginform.html')
    elif session.get('logged_in'):
        return render_template('index.html')
    elif session.get('register_user'):
        return render_template('register.html')
    else:
        return "opps, something went wrong!"

#Login Check
@app.route('/login', methods=['POST', 'GET'])
def do_admin_login():
    if request.method == 'POST':
        if request.form['submit_botton'] == 'Log in':
            name = request.form['username']
            password = request.form['password']

            conn = sqlite3.connect('flask.db')

            c = conn.cursor()

            find_user = ("SELECT * FROM users WHERE username = ? AND password= ?")
            c.execute(find_user, [(name), (password)])
            user = c.fetchall()
            if user:
                session['logged_in'] = True
            else:
                flash('wrong password!')
            return home()
        elif request.form['submit_botton'] == 'Register':
            return render_template('register.html')
        return home()

@app.route('/Games', methods=['GET', 'POST'])
def gaminpedia_info():
    if request.method == 'GET':
        return render_template('gamingpedia.html')

@app.route('/About', methods=['GET', 'POST'])
def about_info():
    if request.method == 'GET':
        return render_template('aboutus.html')


@app.route('/register', methods=['POST', 'GET'])
def do_register():
    if request.method == 'POST':
        if request.form['submit_botton'] == 'Register':
            name = request.form['username']
            password = request.form['password']
            email = request.form['email']

            conn = sqlite3.connect('flask.db')
            c = conn.cursor()

            c.execute("INSERT INTO users (id, username, email, password) VALUES (NULL, ?, ?, ?)",
                      (name, email, password))
            conn.commit()

            c.close()
        return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

"""
Layout.html is the general html code.
Home.css
Loginform/register.html is the html code for log in and register buttons
Rest of html (except loginform/register.html) , follows the same structure as Layout, with some specifications each that is why the need of Block content and end content.

"""


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=5025)
