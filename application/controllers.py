from flask import Flask, render_template, redirect , request
from flask import current_app as app #If we try to import it directly we'll get a circular import error (ERR! Module Not Found Error)
#Essentially this line is a built in pluggin to connect controller.py to app.py

from .models import *
@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/login' , methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form.get('pwd')
        this_user = User.query.filter_by(username = username).first()
        if this_user:
            if this_user.password == pwd:
                if this_user.type == 'admin':
                    return render_template('admin_dash.html', this_user = this_user)
                else:
                    return render_template('user_dash.html', this_user = this_user)
            else:
                return 'Wrong Password'
        else:
            return 'User Doesnt Exist'
    return render_template('login.html')

@app.route('/register' , methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        pwd = request.form['pwd']
        user_name = User.query.filter_by(username = username).first()
        user_email = User.query.filter_by(email = email).first()
        if user_name or user_email:
            return 'User Already Exists'
        else:
            user = User(username = username , email = email , password = pwd)
            db.session.add(user)
            db.session.commit()
        return "registered"    
    return render_template('register.html')

@app.route('/about')
def about():  
    return render_template('about.html')
