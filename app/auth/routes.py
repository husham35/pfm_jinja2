from flask import render_template, redirect, url_for, flash
from . import auth
from .forms import LoginForm, RegistrationForm
from ..models import User
from ..extensions import db
from flask_login import login_user, logout_user, login_required

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and user.check_password(form.password.data):
			login_user(user)
			return redirect(url_for('main.index'))
		flash('Invalid email or password')
	return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email=form.email.data, username=form.username.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Registration successful')
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html', form=form)

