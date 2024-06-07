<<<<<<< HEAD
from flask import Blueprint, render_template
from flask_login import login_required
from .controllers import UserController
=======
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.controllers.Usercontroller import UserController
>>>>>>> a2dae55 (commit)

web = Blueprint('web', __name__)

@web.route('/')
def index():
<<<<<<< HEAD
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

=======
    logged_in = current_user.is_authenticated
    return render_template('sections/home/home.html', logged_in=logged_in)

@web.route('/dashboard')
@login_required
def dashboard():
    return render_template('sections/users/dashboard.html')

@web.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return redirect(url_for('web.dashboard'))
    return UserController.login()

@web.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return redirect(url_for('web.dashboard'))
    return UserController.signup()

>>>>>>> a2dae55 (commit)
@web.route('/logout')
@login_required
def logout():
    return UserController.logout()
<<<<<<< HEAD

=======
>>>>>>> a2dae55 (commit)
