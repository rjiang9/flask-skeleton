from flask import render_template
from flask_login import login_required, current_user
from ..spec.models import Spec
from ..category.models import Category
from . import home_bp
from datetime import datetime

@home_bp.route('/home')
@login_required
def homepage():
    user = current_user
    specs= Spec.query.filter_by(author=user)
    # specs= Spec.query.all()
    date= datetime.now()
    now= date.strftime("%Y-%m-%d")

    return render_template('home/home.html', title='Home Page',
                            specs=specs,
                            DateNow = now)
