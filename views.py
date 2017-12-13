from flask import render_template, redirect, url_for, request
from test import app
from models import User


@app.route('/')
def index():
    myUser = User.query.all()
    return render_template('index.html', t_myUser=myUser)


@app.route('/post_user', methods=['POST'])
def post_user():
    User(request.form['username'], request.form['email'])
    return redirect(url_for('index'))
