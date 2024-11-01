from flask import Blueprint, render_template
from .models import Concert
from . import db


mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    home = db.session.scalars(db.select(Concert)).all()    
    return render_template('index.html', concert=home)

@mainbp.route('/bookings', methods = ['GET', 'POST'])
def bookings():
    return render_template('bookings.html')

