import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import render_template, request, session
from data import *
from datetime import datetime

app = Flask(__name__)

# Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.app_context().push()

db.init_app(app)
db.create_all()

# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/admin")
def admin():
    users = User.query.order_by("timestamp").all()
    return render_template("admin.html", users = users)

@app.route("/registration", methods = ['GET', 'POST'])
def register():
    if request.method=="POST":
        name = request.form.get("name")
        print(name)
        password = request.form.get("Password")
        print(password)
        regist = User(username = name, password = password)
        if User.query.get(name):
            return render_template("registration.html", name1 = name)
        db.session.add(regist)
        db.session.commit()
        return render_template("registration.html", name = name)
    return render_template("registration.html")

@app.route("/auth", methods = ['GET', 'POST'])
def auth():
    if(request.method=="POST"):
        name = request.form.get("name")
        print(name)
        password = request.form.get("Password")
        print(password)
        obj = User.query.get(name)
        if obj is None:
            return render_template("registration.html", message = "Invalid Credentials")
        if (obj.username == name and obj.password == password):
            return render_template("login.html", name=name)
        if (obj.username != name or obj.password != password):
            return render_template("registration.html", message = "Invalid Credentials")
    return render_template("registration.html", message = "Invalid Credentials")

@app.route("/logout")
def logout():
    session.clear()
    return render_template("registration.html")
