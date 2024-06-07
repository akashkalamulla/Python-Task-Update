from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.controllers.Usercontroller import UserController

web = Blueprint('web', __name__)

@web.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('sections/home/home.html', logged_in=True)
    else:
        return render_template('sections/home/home.html', logged_in=False)

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

@web.route('/logout')
@login_required
def logout():
    return UserController.logout()
