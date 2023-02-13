from flask import Flask, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key ='hello'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

from brs.routes import adminRoutes







