from flask import Blueprint, render_template

mainbp = Blueprint('main', __name__)

@mainbp.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@mainbp.route('/bookings', methods = ['GET', 'POST'])
def bookings():
    return render_template('bookings.html')

