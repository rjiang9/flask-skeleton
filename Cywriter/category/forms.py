from flask_wtf import FlaskForm
from wtforms import StringField, TimeField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from .models import Category

class CategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add Type')

