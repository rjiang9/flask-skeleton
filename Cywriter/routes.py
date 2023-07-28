from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required
from Cywriter import app, db
from .spec.models import Spec

@app.route('/')
def index():
    specs= Spec.query.all()
    return render_template('index.html', title='Cywriter | Spec Management System', specs=specs)



