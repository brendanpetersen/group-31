from flask import Blueprint, render_template, redirect, url_for, flash, session
from .forms import LoginForm, RegisterForm

# create login/register blueprint
authbp = Blueprint('auth', __name__ )

@authbp.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        print('Successfully logged in')
        flash('You logged in successfully')
        return redirect(url_for('auth.login'))
    return render_template('user.html', form=loginForm,  heading='Login')

@authbp.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print('Successfully registered')
        return redirect(url_for('auth.login'))
    return render_template('user.html', form=form, heading="Register")

@authbp.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email')
    return 'User logged out'