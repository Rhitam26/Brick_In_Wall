from flask import render_template, flash
from brs.models import admin
from brs.forms import adminForm
from brs import app

@app.route('/')
def homePage():
    return "Hello"
