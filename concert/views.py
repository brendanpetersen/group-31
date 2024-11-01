from flask import Blueprint, render_template, request, redirect, url_for
from .models import Concert
from . import db

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    home = db.session.scalars(db.select(Concert)).all()    
    return render_template('index.html', concert=home)

@mainbp.route('/bookings', methods=['GET', 'POST'])
def bookings():
    return render_template('bookings.html')

@mainbp.route('/search')
def search():
    search_term = request.args.get('search', '')  # Use .get() to avoid KeyError
    if search_term:
        print(search_term)
        query = f"%{search_term}%"
        concert_search = db.session.scalars(db.select(Concert).where(Concert.description.like(query))).all()
        return render_template('index.html', concert=concert_search)
    else:
        return redirect(url_for('main.index'))

