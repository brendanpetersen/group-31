from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, DateField, FileField, PasswordField, IntegerField, DecimalField
from wtforms.validators import InputRequired, Email, EqualTo

#Create event form
class ConcertForm(FlaskForm):
  name = StringField('Concert', validators=[InputRequired()])
  description = TextAreaField('Description', validators = [InputRequired()])
  venue = TextAreaField('Venue', validators = [InputRequired()])
  date = DateField('Date', format='%Y-%m-%d', validators=[InputRequired()])
  time = StringField('Time', validators=[InputRequired()])
  price = DecimalField('Price', validators=[InputRequired()])
  image = FileField('Cover Image', validators=[InputRequired()])
  submit = SubmitField("Create")

#Comment form   
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Post')

# User login
class LoginForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

# User register
class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    fname = StringField("First Name", validators=[InputRequired()])
    surname = StringField("Last Name", validators=[InputRequired()])
    phone = IntegerField("Phone Number", validators=[InputRequired()])
    address = StringField("Address", validators=[InputRequired()])

    # linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    # submit button
    submit = SubmitField("Register")