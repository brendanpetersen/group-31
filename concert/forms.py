import re
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, DateField, FileField, PasswordField, IntegerField, DecimalField
from wtforms.validators import InputRequired, Email, EqualTo, ValidationError

# Custom validators
def validate_email(form, field):
    if '@' not in field.data:
        raise ValidationError('Email must contain an @ symbol.')

def validate_phone(form, field):
    if not (field.data.isdigit() and len(field.data) == 10):
        raise ValidationError('Phone number must be exactly 10 digits.')

def validate_password(form, field):
    password = field.data
    if (len(password) < 8 or 
        not re.search(r"[A-Za-z]", password) or 
        not re.search(r"\d", password) or 
        not re.search(r"[!@#$%^&*()_+]", password)):
        raise ValidationError('Password must be at least 6 characters long, contain at least one letter, one number, and one special character.')

class ConcertForm(FlaskForm):
    name = StringField('Concert', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    venue = TextAreaField('Venue', validators=[InputRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[InputRequired()])
    time = StringField('Time', validators=[InputRequired()])
    price = DecimalField('Price', validators=[InputRequired()])
    image = FileField('Cover Image', validators=[InputRequired()])
    submit = SubmitField("Create")

class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Post')

class LoginForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[InputRequired(), Email("Please enter a valid email"), validate_email])
    fname = StringField("First Name", validators=[InputRequired()])
    surname = StringField("Last Name", validators=[InputRequired()])
    phone = StringField("Phone Number", validators=[InputRequired(), validate_phone])  # Use StringField for validation
    address = StringField("Address", validators=[InputRequired()])

    password = PasswordField("Password", validators=[InputRequired(), validate_password])
    confirm = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo('password', message="Passwords should match")])
    submit = SubmitField("Register")