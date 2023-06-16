from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
#from .models import Category
from ..category.models import Category
from ..models import Spec
from . import task
from .forms import TaskForm
from .. import db
from datetime import datetime

@task.route('/create-task', methods=['GET', 'POST'])
@login_required
def tasks():
    check= None
    user = current_user
    spec= Spec.query.filter_by(author=user)
    date= datetime.now()
    now= date.strftime("%Y-%m-%d")

    form= TaskForm()
    #form.category.choices =[(category.id, category.name) for category in Category.query.all()]
    form.category.choices =[(category.id, category.name) for category in Category.query.all()]

    if request.method == "POST":
        if request.form.get('taskDelete') is not None:
            deleteTask = request.form.get('checkedbox')
            if deleteTask is not None:
                spec = Spec.query.filter_by(id=int(deleteTask)).one()
                db.session.delete(spec)
                db.session.commit()
                return redirect(url_for('task.tasks'))
            else:
                check = 'Please check-box of task to be deleted'

        elif form.validate_on_submit():
            selected= form.category.data
            category = Category.query.get(selected)
            spec = Spec(title=form.title.data, date=form.date.data, time= form.time.data, category=category.name, author=user)
            db.session.add(spec)
            db.session.commit()
            flash('Congratulations, you just added a new note')
            return redirect(url_for('task.tasks'))

    return render_template('task/tasks.html', title='Create Tasks', form=form, spec=spec, DateNow=now, check=check)