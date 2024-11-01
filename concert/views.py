from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from .models import Concert, Booking
from . import db

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    home = db.session.scalars(db.select(Concert)).all()
    return render_template('index.html', concert=home, user=current_user)  # Pass current_user to the template

@mainbp.route('/bookings', methods=['GET', 'POST'])
@login_required
def bookings():
    user_bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template('bookings.html', bookings=user_bookings)

@mainbp.route('/search')
def search():
    search_term = request.args.get('search', '')  # Use .get() to avoid KeyError
    if search_term:
        print(search_term)
        query = f"%{search_term}%"
        concert_search = db.session.scalars(db.select(Concert).where(Concert.description.like(query))).all()
        return render_template('index.html', concert=concert_search, user=current_user)  # Pass current_user to the template
    else:
        return redirect(url_for('main.index'))

@mainbp.route('/book_tickets/<int:id>', methods=['POST'])
@login_required
def book_tickets(id):
    concert = Concert.query.get_or_404(id)
    num_guests = request.form.get('num_guests', type=int)

    if num_guests:
        booking = Booking(
            concert_id=concert.id,
            date=concert.date,
            time=concert.time,
            event_title=concert.name,
            user_id=current_user.id,
            price=concert.price * num_guests,  # Assuming you want to multiply by the number of guests
            num_guests=num_guests
        )
        db.session.add(booking)
        db.session.commit()
        flash('Tickets purchased successfully!', 'success')
        return redirect(url_for('main.bookings'))
    else:
        flash('Please select a number of guests.', 'warning')
        return redirect(url_for('main.show', id=concert.id))