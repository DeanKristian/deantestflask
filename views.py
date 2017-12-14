from flask import render_template, redirect, url_for, request
from test import app
from models import User


@app.before_first_request
def create_all():
    from models import db
    db.create_all()


@app.route('/')
def index():
    myUser = User.query.all()
    User.query.filter_by(username='a').first()
    return render_template('index.html', myUser=myUser)


@app.route('/post_user', methods=['POST'])
def post_user():
    User(request.form['username'], request.form['email'])
    #db.sesson.add(User)
    #db.session.commit()
    return redirect(url_for('index'))


@app.route('/user_page')
def user_page():
    return render_template('usermain.html')
