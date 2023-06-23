from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from .models import It
from .forms import ItForm
from . import it
from .. import db
from datetime import datetime

@it.route('/create-step', methods=['GET', 'POST'])
@login_required
def its():
    check = None
    user = current_user
    it = It.query.all()

    print('hello')
    print(it)

    form = ItForm()

    if request.method == "POST":
        if request.form.get('itDelete') is not None:
            deleteIt = request.form.get('checkedbox')
            if deleteIt is not None:
                it = It.query.filter_by(id=int(deleteIt)).one()
                db.session.delete(it)
                db.session.commit()
                return redirect(url_for('it.its'))
            else:
                check = 'Please check-box of its to be deleted'

        elif form.validate_on_submit():
            it = It(name=form.name.data)
            db.session.add(it)
            db.session.commit()
            flash('Congratulations, you just added a new it(test)')
            return redirect(url_for('it.its'))

    return render_template('it/its.html', title='Create it(test)', form=form, it=it, check=check)
