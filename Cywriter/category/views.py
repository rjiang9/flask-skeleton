from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from .models import Category
from .forms import CategoryForm
from . import category_bp
from .. import db
from datetime import datetime

@category_bp.route('/create-category', methods=['GET', 'POST'])
@login_required
def categories():
    check = None
    user = current_user
    categories = Category.query.all()

    print('h1')
    print(categories)
    print('hello')

    form = CategoryForm()

    if request.method == "POST":
        if request.form.get('categoryDelete') is not None:
            deleteCategory = request.form.get('checkedbox')
            if deleteCategory is not None:
                category = Category.query.filter_by(id=int(deleteCategory)).one()
                db.session.delete(category)
                db.session.commit()
                return redirect(url_for('category_bp.categories'))
            else:
                check = 'Please check-box of category to be deleted'
        elif form.validate_on_submit():
            category = Category(name=form.name.data)
            db.session.add(category)
            db.session.commit()
            flash('Congratulations, you just added a new category')
            return redirect(url_for('category_bp.categories'))

    return render_template('category/categories.html', title='Create categories', form=form, categories=categories, check=check)
