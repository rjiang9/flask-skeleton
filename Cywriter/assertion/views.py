from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from .models import Assertion
from .forms import AssertionForm
from . import assertion_bp
from .. import db
from datetime import datetime

@assertion_bp.route('/create-assertion', methods=['GET', 'POST'])
@login_required
def assertions():
    check = None
    user = current_user
    assertions = Assertion.query.all()

    print('hello')
    print(assertions)

    form = AssertionForm()

    if request.method == "POST":
        if request.form.get('assertionDelete') is not None:
            deleteAssertion = request.form.get('checkedbox')
            if deleteAssertion is not None:
                assertion = Assertion.query.filter_by(id=int(deleteAssertion)).one()
                db.session.delete(assertion)
                db.session.commit()
                return redirect(url_for('assertion_bp.assertions'))
            else:
                check = 'Please check-box of assertion to be deleted'

        elif form.validate_on_submit():
            assertion = Assertion(name=form.name.data)
            db.session.add(assertion)
            db.session.commit()
            flash('Congratulations, you just added a new assertion')
            return redirect(url_for('assertion_bp.assertions'))

    return render_template('assertion/assertions.html', title='Create assertion', form=form, assertions=assertions, check=check)
