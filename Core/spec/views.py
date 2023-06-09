from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from .models import Category
from ..models import Spec
from . import spec
from .forms import SpecForm
from .. import db
from datetime import datetime

@spec.route('/create-spec', methods=['GET', 'POST'])
@login_required
def specs():
    check= None
    user = current_user
    spec= Spec.query.filter_by(author=user)
    date= datetime.now()
    now= date.strftime("%Y-%m-%d")

    form= SpecForm()
    form.category.choices =[(category.id, category.name) for category in Category.query.all()]

    if request.method == "POST":
        if request.form.get('specDelete') is not None:
            deleteSpec = request.form.get('checkedbox')
            if deleteSpec is not None:
                spec = Spec.query.filter_by(id=int(deleteSpec)).one()
                db.session.delete(spec)
                db.session.commit()
                return redirect(url_for('spec.specs'))
            else:
                check = 'Please check-box of spec to be deleted'

        elif form.validate_on_submit():
            selected= form.category.data
            category= Category.query.get(selected)
            spec = Spec(title=form.title.data, date=form.date.data, time= form.time.data, category= category.name, author=user)
            db.session.add(spec)
            db.session.commit()
            flash('Congratulations, you just added a new note')
            return redirect(url_for('spec.specs'))

    return render_template('spec/specs.html', title='Create specs', form=form, spec=spec, DateNow=now, check=check)
