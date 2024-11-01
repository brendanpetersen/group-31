from flask import Blueprint, render_template
from .models import Concert, Comment

#create blueprint for created events
eventbp = Blueprint('upcoming', __name__, url_prefix='/events')

@eventbp.route('/<id>')
def show(id):
    Concert = get_concert()
    return render_template('events/show.html', concert=Concert)

def get_concert():
    b_desc = """American musician with a blend of country and hip-hop; 'Start a Riot' was included in Spider-Man: Into the Spider-Verse."""
    image_loc = 'static/img/shaboozey.webp'  # Adjusted to include the static folder
    concert = Concert('Shaboozey', b_desc, 'The Triffid, Newstead', '21/11/2024', '20:00', image_loc, '$120')
    
    # Set comments
    comments = [
        Comment("Sam", "I've booked already!", '2024-08-12 11:00:00'),
        Comment("Juliette", "purr slay queen", '2024-08-12 11:00:00'),
        Comment("Sally", "hurray", '2024-08-12 11:00:00')
    ]
    for comment in comments:
        concert.set_comments(comment)
    
    return concert