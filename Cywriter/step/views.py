from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from .models import Step
from .forms import StepForm
from . import step_bp
from .. import db
from datetime import datetime

@step_bp.route('/create-step', methods=['GET', 'POST'])
@login_required
def steps():
    check = None
    user = current_user
    steps = Step.query.all()

    form = StepForm()

    if request.method == "POST":
        if request.form.get('stepDelete') is not None:
            deleteStep = request.form.get('checkedbox')
            if deleteStep is not None:
                step = Step.query.filter_by(id=int(deleteStep)).one()
                db.session.delete(step)
                db.session.commit()
                return redirect(url_for('step_bp.steps'))
            else:
                check = 'Please check-box of step to be deleted'

        elif form.validate_on_submit():
            step= Step(name=form.name.data)
            db.session.add(step)
            db.session.commit()
            flash('Congratulations, you just added a new step')
            return redirect(url_for('step_bp.steps'))

    return render_template('step/steps.html', title='Create step', form=form, steps=steps, check=check)
