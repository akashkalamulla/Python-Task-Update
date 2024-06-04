from flask import Blueprint, render_template
from flask_login import login_required
from .controllers import UserController

web = Blueprint('web', __name__)

@web.route('/')
def index():
    return render_template('sections/home/index.html')


@web.route('/dashboard')
@login_required  # Protect this route
def dashboard():
    return UserController.dashboard()

@web.route('/user/<username>')
def user_profile(username):
    return render_template('sections/users/user_profile.html', username=username)


@web.route('/submit', methods=['GET', 'POST'])
def submit():
    return UserController.submit()

@web.route('/login', methods=['GET', 'POST'])
def login():
    return UserController.login()

@web.route('/logout')
@login_required
def logout():
    return UserController.logout()

