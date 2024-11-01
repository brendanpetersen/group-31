from flask import Blueprint, render_template
from .models import Concert, Comment

#create blueprint for created events
eventbp = Blueprint('upcoming', __name__, url_prefix='/events')

@eventbp.route('/<id>')
def show(id):
    return render_template('events/show.html')

def get_concert():
  b_desc = """American musician with a blend of country and hip-hop; 'Start a Riot' was included in Spider-Man: Into the Spider-Verse."""
  image_loc = 'img/shaboozey.webp'
  Concert = Concert('Shaboozey', b_desc,image_loc, 'The Triffid, Newstead', '21/11/2024 20:00', '$120')
  # a comment
  comment = Comment("Sam", "I've booked already!", '2024-08-12 11:00:00')
  Concert.set_comments(comment)
  comment = Comment("Juliette", "purr slay queen", '2024-08-12 11:00:00')
  Concert.set_comments(comment)
  comment = Comment("Sally", "hurray", '2024-08-12 11:00:00')
  Concert.set_comments(comment)
  return Concert