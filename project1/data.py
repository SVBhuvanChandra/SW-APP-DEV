from flask_sqlalchemy import flask_sqlalchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "userdata"
    username = db.Column(db.String, primary_key = True)
    password = db.Column(db.String, nullable = False)
    timestamp = db.Column(db.DateTime, nullable = False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.timestamp = datetime.now()


