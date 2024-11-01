from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Concert, Comment
from .forms import ConcertForm
from werkzeug.utils import secure_filename
import os

#create blueprint for created events
eventbp = Blueprint('upcoming', __name__, url_prefix='/events')

@eventbp.route('/<id>')
def show(id):
    Concert = get_concert()
    return render_template('events/show.html', concert=Concert)

@eventbp.route('/create', methods = ['GET', 'POST'])
def create():
  print('Method type: ', request.method)
  form = ConcertForm()
  if form.validate_on_submit():
    print('Successfully created new event')
    
    image_file = form.image.data
    filename = secure_filename(image_file.filename)
        
    upload_path = os.path.join('/img', filename)
        
    image_file.save(upload_path)

    concert = Concert(
        name=form.name.data,
        description=form.description.data,
        venue=form.venue.data,
        date=form.date.data,
        time=form.time.data,
        price=form.price.data,
        image=upload_path
        )

    print(concert)

    flash('Event created successfully!', 'success')
    return redirect(url_for('upcoming.show', id=1))

  return render_template('events/create.html', form=form)

def get_concert():
    b_desc = """American musician with a blend of country and hip-hop; 'Start a Riot' was included in Spider-Man: Into the Spider-Verse."""
    image_loc = 'img/shaboozey.webp'
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