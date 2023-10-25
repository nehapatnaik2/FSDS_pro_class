#session is an active period of interaction between the user and the application.
# The entirety of the session is the time the user spends on an application from logging in to logging out.

from flask import session
from flask import Flask, render_template, request, redirect, url_for
from datetime import timedelta

app = Flask(__name__)
#The secret key is set to "MY_SECRET_KEY" by calling the app object’s secret_key attribute
app.secret_key = 'MY_SECRET_KEY'

#How long do you want your per session to be
app.permanent_session_lifetime(timedelta(minutes=1))
#The session timeout is set to one minute (timedelta(minutes=1)) by calling the app object’s permanent_session_lifetime.
#  After one minute, the active sessions will be terminated automatically.
@app.route("/")
def home():
    return render_template('home.html')

# Resgistering user name:
@app.route('/add', methods = ['GET','POST'])
def add_user():
    session['message'] = "Enter your username to continue."
    if request.method == 'POST':
        username = request.form['username']
        session['user'] = username
        session['greet'] = f"Successfully registered username - {session['user']}."
        return redirect(url_for("home"))
 
    return render_template("add_username.html")

    #removing user name
@app.route('/remove')
def remove():
    session.pop('user')  
    session['notify'] = f'user name removed from session storage' 
    return redirect(url_for('home'))

#----------------------------------------------------------------------------
#Flask -Session
#extension of Flask that offers extra support for managing sessions in the Flask application. 
# It is designed to enhance the capability of session handling by providing various session storage types and configurations in Flask.
from flask import session
from flask_session import Session
from flask import Flask, render_template, request, redirect, url_for
 
# Creating Flask App
app = Flask(__name__)
# Setting up Secret Key for Session Management
app.secret_key = "MY_SECRET_KEY"
 
# Configuring Session
app.config['PERMANENT_SESSION_LIFETIME'] = 60  # Session Lifetime
app.config['SESSION_TYPE'] = "filesystem"  # Session Storage Type
 
# Path to Storing Session
app.config['SESSION_FILE_DIR'] = "session_data"
 
# Initializing the Session Extension
Session(app)