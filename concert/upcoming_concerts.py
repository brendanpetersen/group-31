from flask import Blueprint, render_template

#create blueprint for created events
eventbp = Blueprint('upcoming', __name__, url_prefix='/events')

@eventbp.route('/fred-again', methods = ['GET', 'POST'])
def fred_again():
    return render_template('events/fred-again.html')

@eventbp.route('/sabrina-carpenter', methods = ['GET', 'POST'])
def sabrina_carpenter():
    return render_template('events/sabrina-carpenter.html')

@eventbp.route('/shaboozey', methods = ['GET', 'POST'])
def shaboozey():
    return render_template('events/shaboozey.html')

@eventbp.route('/them-dirty-roses', methods = ['GET', 'POST'])
def them_dirty_roses():
    return render_template('events/them-dirty-roses.html')