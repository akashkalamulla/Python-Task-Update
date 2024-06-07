<<<<<<< HEAD
from flask import render_template, request, redirect, url_for, flash
from ..models.user import db, User
from flask_login import login_user, logout_user, current_user
from app import bcrypt
from ..forms.auth import RegistrationForm, LoginForm

def dashboard():
    if not current_user.is_authenticated:
        return redirect(url_for('web.login'))
    user = User.query.filter_by(email=current_user.email, phone=current_user.phone).first()
    return render_template('sections/users/dashboard.html', user=user)

def submit():
    if current_user.is_authenticated:
        return redirect(url_for('web.dashboard'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        phone = form.phone.data
        password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists.', 'danger')
            return redirect(url_for('web.submit'))

        new_user = User(username=username, email=email, phone=phone, password=password)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully!', 'success')
            return redirect(url_for('web.login'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {e}', 'danger')
            return redirect(url_for('web.submit'))
    return render_template('sections/users/form.html', form=form)

def login():
    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return redirect(url_for('web.dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        email_or_phone = form.email_or_phone.data
        user = User.query.filter((User.email == email_or_phone) | (User.phone == email_or_phone)).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('web.dashboard'))
        else:
            flash('Login failed. Check your phone number or email and Password.', 'danger')

    return render_template('sections/users/login.html', form=form)

def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('web.home'))
=======
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user import User
from app import db, bcrypt
from app.forms.auth import LoginForm, RegistrationForm

class UserController:
    @staticmethod
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('web.dashboard'))

        form = LoginForm()
        if form.validate_on_submit():
            email_or_phone = form.email_or_phone.data
            user = User.query.filter((User.email == email_or_phone) | (User.phone == email_or_phone)).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('web.dashboard'))
            else:
                flash('Login failed. Check your phone number or email and password.', 'danger')

        return render_template('sections/users/login.html', form=form)

    @staticmethod
    def signup():
        if current_user.is_authenticated:
            return redirect(url_for('web.dashboard'))

        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, email=form.email.data, phone=form.phone.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('web.login'))
        
        return render_template('sections/users/signup.html', form=form)

    @staticmethod
    @login_required
    def logout():
        logout_user()
        flash('You have been logged out.', 'info')
        return redirect(url_for('web.index'))
>>>>>>> a2dae55 (commit)
