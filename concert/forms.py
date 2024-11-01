from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, DateField, FileField
from wtforms.validators import InputRequired, Length

class ConcertForm(FlaskForm):
  name = StringField('Concert', validators=[InputRequired()])
  description = TextAreaField('Description', validators = [InputRequired()])
  venue = TextAreaField('Venue', validators = [InputRequired()])
  date = DateField('Date', format='%Y-%m-%d', validators=[InputRequired()])
  time = StringField('Time', validators=[InputRequired()])
  price = StringField('Price', validators=[InputRequired()])
  image = FileField('Cover Image', validators=[InputRequired()])
  submit = SubmitField("Create")
    
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Post')