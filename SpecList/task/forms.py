from flask_wtf import FlaskForm
from wtforms import (StringField, DateField, TimeField,
                     TextAreaField, IntegerField, BooleanField,
                     SelectField, RadioField, SubmitField,
                     EmailField)
from wtforms.validators import (DataRequired, InputRequired,
                                Length, Email, EqualTo, 
                                Optional, URL)
from ..category.models import Category

class TaskForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    baseurl = StringField('BaseUrl', validators=[DataRequired(), URL()])
    category= SelectField('Type', coerce=int, validators=[DataRequired()])
    funtionname = StringField('Function Name', validators=[DataRequired()])
    beforeaction = StringField('Before Action')
    postaction = StringField('Post Action')

    loginrequired = BooleanField('Login Required for the test')

    acct1 = StringField('Test Account 1', validators=[Length(min=3,max=10,message="Account must be between 3 and 10 characters.")])
    acct2 = StringField('Test Account 2', validators=[Optional(), Length(min=3,max=10)])
    acct3 = StringField('Test Account 3', validators=[Optional(), Length(min=3,max=10)])

    email1 = EmailField('Test email1', validators=[Optional(), Email(message="Invalid email")])
    email2 = StringField('Test email2', validators=[Optional(), Email(message="Invalid email")])
    email3 = StringField('Test email3', validators=[Optional(), Email(message="Invalid email")])

    prerequisites = TextAreaField('Prerequisites', validators=[Length(max=200)])

    submit = SubmitField('Save Spec')
