from .extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(50), nullable=False)
	lastname = db.Column(db.String(50), nullable=False)
	username = db.Column(db.String(150), unique=True, nullable=False)
	email = db.Column(db.String(150), unique=True, nullable=False)
	password_hash =  db.Column(db.String(256), nullable=False)

	budgets = db.relationship('Budget', back_populates='user', cascade='all, delete-orphan')
	expenses = db.relationship('Expense', back_populates='user', cascade='all, delete-orphan')
	categories = db.relationship('ExpenseCategory', back_populates='user', cascade='all, delete-orphan')
	items = db.relationship('ExpenseCategoryItem', back_populates='user', cascade='all, delete-orphan')

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
	
