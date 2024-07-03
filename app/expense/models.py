from ..extensions import db


class Expense(db.Model):
	__tablename__ = 'expenses'
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(255), nullable=False)
	amount = db.Column(db.Float, nullable=False)
	# category = db.Column(db.String(80), nullable=False)
	date = db.Column(db.Date, nullable=False)

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	user = db.relationship('User', backref=db.backref('expenses', lazy=True))

	expense_category_id = db.Column(db.Integer, db.ForeignKey('expense_categories.id'), nullable=False)
	expense_category = db.relationship('ExpenseCategory', back_populates='expenses')
    

class ExpenseCategory(db.Model):
	__tablename__ = 'expense_categories'
	id = db.Column(db.Integer, primary_key=True)
	expense_category_name = db.Column(db.String(150), nullable=False)
	description = db.Column(db.String(255), nullable=False)

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	user = db.relationship('User', backref=db.backref('expenses', lazy=True))

	expenses = db.relationship('Expense', back_populates='expense_categories', cascade='all, delete-orphan')
	expense_category_items = db.relationship('ExpenseCategoryItem', back_populates='expense_categories', cascade='all, delete-orphan')
    
    

class ExpenseCategoryItem(db.Model):
	__tablename__ = 'expense_category_items'
	id = db.Column(db.Integer, primary_key=True)
	category_item_name = db.Column(db.String(150), nullable=False)
	expense_category_id = db.Column(db.Integer, db.ForeignKey('expense_category.id'), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	user = db.relationship('User', backref=db.backref('expenses', lazy=True))
	# expense_category = db.relationship('ExpenseCategory', backref=db.backref('expense_categories', lazy=True))

	expense_category_id = db.Column(db.Integer, db.ForeignKey('expense_categories.id'), nullable=False)
	expense_category = db.relationship('ExpenseCategory', back_populates='items')
