from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Concert, Comment, Booking 
from .forms import ConcertForm, CommentForm
from werkzeug.utils import secure_filename
import os
from . import db
from flask_login import login_required, current_user

eventbp = Blueprint('upcoming', __name__, url_prefix='/events')

UPLOAD_FOLDER = 'templates/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@eventbp.route('/<id>')
def show(id):
    concert_instance = db.session.scalar(db.select(Concert).where(Concert.id == id))
    
    if concert_instance is None:
        flash('Concert not found', 'danger')
        return redirect(url_for('main.index'))

    cform = CommentForm()
    return render_template('events/show.html', concert=concert_instance, cform=cform)

@eventbp.route('/<id>/comment', methods=['POST'])
def comment(id):
    form = CommentForm()
    if form.validate_on_submit():
        user_id = 1
        new_comment = Comment(
            text=form.text.data,
            user_id=user_id,
            concert_id=id
        )
        db.session.add(new_comment)
        db.session.commit()
        flash('Your comment has been added', 'success')
        return redirect(url_for('upcoming.show', id=id))
    
    flash('Failed to post comment. Please try again.', 'danger')
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
            
            concert = Concert(
                name=form.name.data,
                description=form.description.data,
                venue=form.venue.data,
                date=form.date.data,
                time=form.time.data,
                price=form.price.data,
                image=upload_path
            )
            
            db.session.add(concert)
            db.session.commit()
            
            flash('Event created successfully!', 'success')
            return redirect(url_for('upcoming.show', id=concert.id)) 
        else:
            flash('Invalid file type. Please upload an image.', 'danger')

    return render_template('events/create.html', form=form)

@eventbp.route('/<id>/book', methods=['POST'])
@login_required
def book_tickets(id):
    concert = db.session.get(Concert, id)
    if concert is None:
        flash('Concert not found', 'danger')
        return redirect(url_for('main.index'))
    
    num_guests = request.form.get('num_guests', type=int)
    if current_user.is_authenticated:
        booking = Booking(
            date=concert.date,
            time=concert.time,
            event_title=concert.name,
            user=current_user, 
            price=concert.price,
            num_guests=num_guests
        )
        db.session.add(booking)
        db.session.commit()
        flash('Tickets purchased successfully!', 'success')
        return redirect(url_for('main.bookings'))
    else:
        flash('You need to be logged in to book tickets.', 'danger')
        return redirect(url_for('auth.login'))

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