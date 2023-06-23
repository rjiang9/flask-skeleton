from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
#from .models import Category
from ..category.models import Category
from ..models import Spec
from . import task
from .forms import TaskForm
from .. import db
from datetime import datetime


@task.route('/delete-spec/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_spec(id):
    pass

@task.route('/generate-spec/<int:id>', methods=['GET', 'POST'])
@login_required
def generate_spec(id):
    pass


@task.route('/update-spec/<int:id>', methods=['GET', 'POST'])
@login_required
def update_spec(id):
    check= None
    user = current_user
    spec_obj = Spec.query.get(id)

    form= TaskForm(obj=spec_obj)
    form.category.choices =[(category.id, category.name) for category in Category.query.all()]
    spec= Spec.query.all()

    if form.validate_on_submit():
        form.populated_obj(spec_obj)
        db.session.commit()
        flash('Changes are saved')
        return redirect(url_for('task.tasks'))

    return render_template('task/tasks.html', title='Edit Spec', form=form, spec=spec, check=check)


@task.route('/create-spec', methods=['GET', 'POST'])
@login_required
def tasks():
    check= None
    user = current_user

    # spec= Spec.query.filter_by(author=user)
    spec= Spec.query.all()
    # date= datetime.now()
    # now= date.strftime("%Y-%m-%d")

    print('I am {}'.format(user))

    categories = Category.query.all()
    if not categories:
        flash("please add at least one type")
        return redirect(url_for('category.categories', check="Please add type"))


    form= TaskForm()
    form.category.choices =[(category.id, category.name) for category in Category.query.all()]

    # loginrequired 
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

            # spec = Spec(title=form.title.data, date=form.date.data, time= form.time.data, category=category.name, author=user)
            spec = Spec(
                    name=form.name.data,
                    baseurl=form.baseurl.data,
                    category=category.name,
                    funtionname=form.funtionname.data,
                    beforeaction=form.beforeaction.data,
                    postaction=form.postaction.data,
                    acct1=form.acct1.data,
                    acct2=form.acct2.data,
                    acct3=form.acct3.data,

                    email1=form.email1.data,
                    email2=form.email2.data,
                    email3=form.email3.data,

                    prerequisites=form.prerequisites.data,
                    loginrequired=form.loginrequired.data,
                    author=user)

            db.session.add(spec)
            db.session.commit()
            flash('New spec is added successfully')
            return redirect(url_for('task.tasks'))

    return render_template('task/tasks.html', title='Create Spec', form=form, spec=spec, check=check)
