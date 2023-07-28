from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from .models import Step
from ..spec.models import Spec
from .forms import StepForm
from . import step_bp
from .. import db
from datetime import datetime

@step_bp.route('/steps/<int:spid>')
@login_required
def steps(spid):
    user = current_user
    spec = Spec.query.get(spid)

    steps = Step.query.all() # filter by spec_id, no mater who created

    return render_template('step/steps.html', spec_id=spid, title='Spec steps', spec=spec, steps=steps, user=user)


@step_bp.route('/delete-step/<int:stid>', methods=['GET', 'POST'])
@login_required
def delete_step(stid):
    check= None
    user = current_user
    # spec = Spec.query.filter_by(id=int(id), author=user).one()
    step = Spec.query.get(id=int(stid))
    spec_id = step.spec_id

    if not spec:
        check = 'Delete error, please let administrator know.'
        return redirect(url_for('step_bp.steps', check=check))

    db.session.delete(spec)
    db.session.commit()
    flash("Spec id={} has been deleted".format(stid))

    return redirect(url_for('home_bp.homepage'))


@step_bp.route('/edit-step/<int:stid>', methods=['GET', 'POST'])
@login_required
def edit_step(stid):
    check = None
    user = current_user
    # find spec id by step id
    step = Step.query.filter_by(id=stid)
    spec_id = step.spec_id 
    spec = Spec.query.get(spec_id)


    form = StepForm()

    if request.method == "POST":
        if form.validate_on_submit():
            step= Step(name=form.name.data)
            db.session.add(step)
            db.session.commit()
            flash('New is added in')

            return redirect(url_for('step_bp.steps', spec_id=spec_id))

    return render_template('step/steps.html', title='Create step', form=form, spec=spec, step=step, check=check)


@step_bp.route('/add-step/<int:spid>', methods=['GET', 'POST'])
@login_required
def add_step(spid):
    check = None
    user = current_user
    spec = Spec.query.get(spid)
    print(spec)

    steps = Step.query.all() # filter by spec_id but now with user_id

    print('hello {}'.format(user))
    print(steps)

    form = StepForm()

    if request.method == "POST":
        if form.validate_on_submit():
            step= Step(name=form.name.data)
            db.session.add(step)
            db.session.commit()
            flash('New is added in')

            return redirect(url_for('step_bp.steps'))

    return render_template('step/steps.html', title='Create step', form=form, spec=spec, steps=steps, check=check)



@step_bp.route('/create-step/<int:spid>', methods=['GET', 'POST'])
@login_required
def steps2(spid):
    check = None
    user = current_user
    spec = Spec.query.get(spid)

    steps = Step.query.all()

    print('hello {}'.format(user))
    print(step)

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

    return render_template('step/steps.html', title='Create step', form=form, spec=spec, steps=steps, check=check)



@step_bp.route('/add-step2/<int:spid>', methods=['GET', 'POST'])
@login_required
def add_step2(spid):
    check = None
    user = current_user
    spec = Spec.query.get(spid)

    steps = Step.query.all()

    print('hello {}'.format(user))
    print(step)

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

    return render_template('step/steps.html', title='Create step', form=form, spec=spec, steps=steps, check=check)



