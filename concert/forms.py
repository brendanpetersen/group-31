from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField
from wtforms.validators import InputRequired, Length

class ConcertForm(FlaskForm):
  name = StringField('Concert', validators=[InputRequired()])
  # adding two validators, one to ensure input is entered and other to check if the 
  # description meets the length requirements
  description = TextAreaField('Description', validators = [InputRequired()])
  venue = TextAreaField('Venue', validators = [InputRequired()])
  date = StringField('Date', validators=[InputRequired()])
  time = StringField('Time', validators=[InputRequired()])
  price = StringField('Price', validators=[InputRequired()])
  image = StringField('Cover Image', validators=[InputRequired()])
  submit = SubmitField("Create")
    
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')