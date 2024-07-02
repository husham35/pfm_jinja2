from flask import render_template, redirect, url_for, flash, session, request

from . import auth
from .forms import LoginForm, RegistrationForm, ForgotPasswordForm
from ..models import User
from ..extensions import db
from flask_login import login_user, logout_user, login_required


@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			user = User.query.filter_by(email=form.email.data).first()
			if user and user.check_password(form.password.data):
				login_user(user)
				flash('Logged in successfully', 'success')
				return redirect(url_for('main.dashboard'))
		else:
			flash('Invalid email or password', 'danger')

	return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			user = User(
				firstname=form.firstname.data,
				lastname=form.lastname.data,
				email=form.email.data,
				username=form.username.data,
				)
			user.set_password(form.password.data)
			db.session.add(user)
			db.session.commit()
			flash('Registration successful', 'success')
			return redirect(url_for('auth.login'))
		else:
			flash('Registration failed', 'danger')
	return render_template('auth/register.html', form=form)


@auth.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
	form = ForgotPasswordForm()
	if form.validate_on_submit():
		email = email=form.email.data

		# search for in db

		# if email is found, send password reset link to email
	
		flash('Password reset link successfully sent your email.', 'success')
		return redirect(url_for('auth.login'))
	# supplied email does not exist
	return render_template('auth/forgot-password.html', form=form)

