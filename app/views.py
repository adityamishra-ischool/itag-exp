from app import app
from flask import render_template
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Aditya' } # fake user
    return render_template("index.html",        title = 'Home',
        user = user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
        title = 'Sign In',
        form = form)

@app.route('/adminhome')
def adminhome():
	return render_template('adminpage.html')

@app.route('/addplayer')
def addplayer():
	return render_template('addplayer.html')
@app.route('/updateit')
def updateit():
	return render_template('updateit.html')