from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# A class created to make SQL database.
class User(db.Model):
    __tablename__ = "userdata"
    username = db.Column(db.String, primary_key = True)
    password = db.Column(db.String, nullable = False)
    timestamp = db.Column(db.DateTime, nullable = False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.timestamp = datetime.now()

class Book(db.Model):
    __tablename__ = "book"
    isbn = db.Column(db.String, primary_key = True)
    title = db.Column(db.String, nullable = False)
    author = db.Column(db.String, nullable = False)
    year = db.Column(db.String, nullable = False)

    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year


