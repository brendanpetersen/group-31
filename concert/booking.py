from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Booking 
from . import db

# Create the bookings blueprint
mainbp = Blueprint('main', __name__)

@mainbp.route('/bookings', methods=['GET'])
@login_required
def bookings():
    user_bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template('bookings.html', bookings=user_bookings)