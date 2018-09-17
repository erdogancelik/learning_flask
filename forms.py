from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First name', validators=[DataRequired('Please enter your First Name')])
    last_name = StringField('Last name', validators=[DataRequired('Please enter your Last Name')])
    email = StringField('Email', validators=[DataRequired('Please enter your Email Address'), Email('Please enter your email address')])
    password = PasswordField('Password', validators=[DataRequired('Please enter a Password'), Length(min=6, message='Password must be 6 characters or more')])
    submit = SubmitField('Sign up')
