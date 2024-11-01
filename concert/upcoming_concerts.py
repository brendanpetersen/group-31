from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Concert, Comment
from .forms import ConcertForm, CommentForm
from werkzeug.utils import secure_filename
import os
from . import db

#create blueprint for created events
eventbp = Blueprint('upcoming', __name__, url_prefix='/events')

UPLOAD_FOLDER = 'templates/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@eventbp.route('/<id>')
def show(id):
    concert_instance = db.session.scalar(db.select(Concert).where(Concert.id==id))
    cform = CommentForm()
    return render_template('events/show.html', concert=concert_instance, cform=cform)

@eventbp.route('/<id>/comment', methods=['POST'])
def comment(id):
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(user="Current User", text=form.text.data, created_at='2024-08-12 11:00:00')
        concert = get_concert(int(id))
        if concert:
            concert.set_comments(new_comment)
            flash('Your comment has been posted!', 'success')
        else:
            flash('Concert not found.', 'danger')
    else:
        flash('There was an issue posting your comment.', 'danger')
    return redirect(url_for('upcoming.show', id=id))

@eventbp.route('/create', methods=['GET', 'POST'])
def create():
    form = ConcertForm()
    if form.validate_on_submit():
        image_file = form.image.data

        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            upload_path = os.path.join(UPLOAD_FOLDER, filename)
            image_file.save(upload_path)
            
            # Create a new Concert instance
            concert = Concert(
                name=form.name.data,
                description=form.description.data,
                venue=form.venue.data,
                date=form.date.data,
                time=form.time.data,
                price=form.price.data,
                image=upload_path
            )
            
            # Add the concert to the session and commit
            db.session.add(concert)
            db.session.commit()
            
            flash('Event created successfully!', 'success')
            return redirect(url_for('upcoming.show', id=concert.id))  # Redirect to the new concert's page
        else:
            flash('Invalid file type. Please upload an image.', 'danger')

    return render_template('events/create.html', form=form)

def get_concert(id):
    if id == 1:
        b_desc = """American musician with a blend of country and hip-hop; 'Start a Riot' was included in Spider-Man: Into the Spider-Verse."""
        image_loc = 'img/shaboozey.webp'
        concert = Concert('Shaboozey', b_desc, 'The Triffid, Newstead', '21/11/2024', '20:00', image_loc, '$120')
        concert.id = id 

        # Set comments
        comments = [
            Comment("Sam", "I've booked already!", '2024-08-12 11:00:00'),
            Comment("Juliette", "purr slay queen", '2024-08-12 11:00:00'),
            Comment("Sally", "hurray", '2024-08-12 11:00:00')
        ]
        for comment in comments:
            concert.set_comments(comment)

        return concert
    else:
        return None