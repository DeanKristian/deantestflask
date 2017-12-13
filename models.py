from flask_sqlalchemy import SQLAlchemy
from test import app

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<User %r>' % self.username
