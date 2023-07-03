from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from .models import Selector
from .forms import SelectorForm
from . import selector_bp
from .. import db
from datetime import datetime

@selector_bp.route('/create-selector', methods=['GET', 'POST'])
@login_required
def selectors():
    check = None
    user = current_user
    selectors = Selector.query.all()

    form = SelectorForm()

    if request.method == "POST":
        if request.form.get('selectorDelete') is not None:
            deleteSelector = request.form.get('checkedbox')
            if deleteSelector is not None:
                selector = Selector.query.filter_by(id=int(deleteSelector)).one()
                db.session.delete(selector)
                db.session.commit()
                return redirect(url_for('selector_bp.selectors'))
            else:
                check = 'Please check-box of selector to be deleted'

        elif form.validate_on_submit():
            selector = Selector(name=form.name.data)
            db.session.add(selector)
            db.session.commit()
            flash('Congratulations, you just added a new selector')
            return redirect(url_for('selector_bp.selectors'))

    return render_template('selector/selectors.html', title='Create selectors', form=form, selectors=selectors, check=check)
