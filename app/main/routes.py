from flask import render_template
from . import main
from flask_login import login_required


@main.route('/')
def index():
	return render_template('main/landing.html')


@main.route('/profile')
@login_required
def profile():
	return render_template('main/profile.html')

@main.route('/dashboard')
@login_required
def dashboard():
	return render_template('main/dashboard.html')
