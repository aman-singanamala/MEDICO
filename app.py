from flask import Flask, url_for, redirect, render_template, url_for, session, logging
app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/sign_log')
def signup():
    return render_template('signup.html')
@app.route('/diabetes')
def diabetes():
    return render_template('diabetes.html')
@app.route('/heart')
def heart():
    return render_template('heart.html')



