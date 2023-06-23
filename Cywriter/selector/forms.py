from flask_wtf import FlaskForm
from wtforms import StringField, TimeField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from .models import Selector

class SelectorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add Selector')

