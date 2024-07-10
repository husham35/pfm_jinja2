from ..extensions import db


class Expense(db.Model):
	__tablename__ = 'expenses'
	id = db.Column(db.Integer, primary_key=True)
	amount = db.Column(db.Float, nullable=False)
	date = db.Column(db.Date, nullable=False)
	description = db.Column(db.String(255), nullable=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id', name='fk_expenses_user_id'), nullable=False)
	budget_id = db.Column(db.Integer, db.ForeignKey('budgets.id', name='fk_expenses_budget_id'), nullable=False)
	category_id = db.Column(db.Integer, db.ForeignKey('expense_categories.id', name='fk_expenses_category_id'), nullable=False)
	category_item_id = db.Column(db.Integer, db.ForeignKey('expense_category_items.id', name='fk_expenses_category_item_id'), nullable=False)

	user = db.relationship('User', back_populates='expenses')
	budget = db.relationship('Budget', back_populates='expenses')
	category = db.relationship('ExpenseCategory', back_populates='expenses')
	category_item = db.relationship('ExpenseCategoryItem', back_populates='expenses')
    

class ExpenseCategory(db.Model):
	__tablename__ = 'expense_categories'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id', name='fk_expense_categories_user_id'), nullable=False)

	user = db.relationship('User', back_populates='categories')
	expenses = db.relationship('Expense', back_populates='category', cascade='all, delete-orphan')
	items = db.relationship('ExpenseCategoryItem', back_populates='category', cascade='all, delete-orphan')
    

class ExpenseCategoryItem(db.Model):
	__tablename__ = 'expense_category_items'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	category_id = db.Column(db.Integer, db.ForeignKey('expense_categories.id', name='fk_expense_category_items_category_id'), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id', name='fk_expense_category_items_user_id'), nullable=False)

	category = db.relationship('ExpenseCategory', back_populates='items')
	user = db.relationship('User', back_populates='items')
	expenses = db.relationship('Expense', backref='item', lazy=True)

