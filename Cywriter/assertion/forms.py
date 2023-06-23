from flask_wtf import FlaskForm
from wtforms import StringField, TimeField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from .models import Assertion

class AssertionForm(FlaskForm):
    name = StringField('Assertion Name', validators=[DataRequired()])
    submit = SubmitField('Add Assertion')

