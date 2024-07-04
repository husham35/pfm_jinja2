from ..extensions import db


class Expense(db.Model):
	__tablename__ = 'expenses'
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(255), nullable=False)
	amount = db.Column(db.Float, nullable=False)
	# category = db.Column(db.String(80), nullable=False)
	date = db.Column(db.Date, nullable=False)

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	budget_id = db.Column(db.Integer, db.ForeignKey('budgets.id'), nullable=False)
	category_id = db.Column(db.Integer, db.ForeignKey('expense_categories.id'), nullable=False)

	user = db.relationship('User', back_populates='expenses')
	budget = db.relationship('Budget', back_populates='expenses')
	category = db.relationship('ExpenseCategory', back_populates='expenses')
    

class ExpenseCategory(db.Model):
	__tablename__ = 'expense_categories'
	id = db.Column(db.Integer, primary_key=True)
	expense_category_name = db.Column(db.String(150), nullable=False)
	description = db.Column(db.String(255), nullable=False)

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

	user = db.relationship('User', back_populates='categories')
	expenses = db.relationship('Expense', back_populates='category', cascade='all, delete-orphan')
	items = db.relationship('ExpenseCategoryItem', back_populates='category', cascade='all, delete-orphan', foreign_keys='ExpenseCategoryItem.category_id')
    
    

class ExpenseCategoryItem(db.Model):
	__tablename__ = 'expense_category_items'
	id = db.Column(db.Integer, primary_key=True)
	category_item_name = db.Column(db.String(150), nullable=False)

	category_id = db.Column(db.Integer, db.ForeignKey('expense_categories.id', name='fk_expense_category_items_category_id'), nullable=False)

	category = db.relationship('ExpenseCategory', back_populates='items', foreign_keys=[category_id])
