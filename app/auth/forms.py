from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, InputRequired, Email, EqualTo, Length, ValidationError

from ..models import User


def username_exists(form, field):
    if User.query.filter_by(username=field.data).first():
        raise ValidationError('Username already in use.')

def email_exists(form, field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError('Email already in use.')


class LoginForm(FlaskForm):
	email =  StringField('Email', validators=[DataRequired(), Email()])
	password =  PasswordField('Password', validators=[DataRequired()])
	submit =SubmitField('Login')


class RegistrationForm(FlaskForm):
	firstname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=40)])
	lastname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=40)])
	email = StringField('Email', validators=[DataRequired(), Email(), email_exists])
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20), username_exists])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	terms = BooleanField('I accept the terms and privacy policy')
	submit = SubmitField('Register')

	def validate_terms(form, field):
		if not field.data:
			raise ValidationError('You must agree to the terms and conditions')


class ForgotPasswordForm(FlaskForm):
	email =  StringField('Email', validators=[DataRequired(), Email()])
	submit =SubmitField('Login')