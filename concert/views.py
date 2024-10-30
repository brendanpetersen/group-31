from flask import Blueprint, render_template, request, session

mainbp = Blueprint('main', __name__)

@mainbp.route('/login', methods = ['GET', 'POST'])
def login():
    print("Login route called")
    email = request.values.get("email")
    password = request.values.get("password")
    print (f"Email: {email}\nPassword: {password}")
    session['email'] = request.values.get('email')
    return render_template('login.html')

@mainbp.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@mainbp.route('/bookings', methods = ['GET', 'POST'])
def bookings():
    return render_template('bookings.html')

@mainbp.route('/create', methods = ['GET', 'POST'])
def create_event():
    return render_template('create-event.html')

@mainbp.route('/register', methods = ['GET', 'POST'])
def register():
    email = request.values.get("email")
    password = request.values.get("password")
    username = request.values.get("username")
    fname = request.values.get("first_name")
    surname = request.values.get("surname")
    number = request.values.get("contact_number")
    address = request.values.get("street_address")
    print (f"Email: {email}\nPassword: {password}\nusername: {username}\nFirst Name: {fname}\nSurname: {surname}\nPhone: {number}\nAddress: {address}")
    session['email'] = request.values.get('email')
    return render_template('register.html')

@mainbp.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email')
    return 'User logged out'