from ..extensions import db


class Budget(db.Model):
	__tablename__ = 'budgets'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), nullable=False)
	start_date = db.Column(db.Date, nullable=False)
	end_date = db.Column(db.Date, nullable=False)
	amount = db.Column(db.Float, nullable=False)
	
	user_id = db.Column(db.Integer, db.ForeignKey('users.id', name='fk_budgets_user_id'), nullable=False)

	user = db.relationship('User', back_populates='budgets')
	expenses = db.relationship('Expense', back_populates='budget', cascade='all, delete-orphan')
