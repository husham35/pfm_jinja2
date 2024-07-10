from flask import render_template, redirect, url_for, flash, session, request

from . import expense
from ..extensions import db
from .models import Expense, ExpenseCategory, ExpenseCategoryItem
from .forms import CreateExpenseForm

from flask_login import login_required, current_user

@expense.route('/expenses', strict_slashes=False, methods=['GET'])
@expense.route('/expenses/<int:expense_id>')
@login_required
def expenses(expense_id=None):
	user_id = current_user.id
	form = CreateExpenseForm()
	
	# get all expenses
	all_expenses = Expense.query.filter_by(user_id=user_id).all()

	if expense_id:
		single_expense = Expense.query.get_or_404(expense_id)
		return render_template('expense/view.html', expense=single_expense, form=form)
	# else:
	return render_template('expense/index.html', expenses=all_expenses)


@expense.route('/expenses/create', methods=['GET', 'POST'])
@login_required
def create_expense():
	form = CreateExpenseForm()
	user_id = current_user.id
	if request.method == 'POST':
		if form.validate_on_submit():
			expense = Expense(
				amount=float(form.amount.data),
				date=form.date.data,
				description=form.description.data,
				budget_id=form.budget_id.data,
				category_id=form.category_id.data,
				category_item_id=form.category_item_id.data,
				user_id=user_id,
			)
			db.session.add(expense)
			db.session.commit()
			flash('Expense added successfully', 'success')
			return redirect(url_for('expense.expenses'))
		else:
			flash('Failed to save expense', 'warning')

	return render_template('expense/create.html', form=form)


@expense.route('/expenses/<int:expense_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_expense(expense_id):
	# user_id = current_user.id
	expense = Expense.query.get_or_404(expense_id)

	form = CreateExpenseForm(obj=expense)

	if request.method == 'POST':
		if form.validate_on_submit():

			form.populate_obj(expense)
			db.session.commit()
			flash('Expense updated successfully', 'success')
			return redirect(url_for('expense.expenses'))
		else:
			flash('Failed to update expense', 'warning')

	return render_template('expense/update.html', expense=expense, form=form)


@expense.route('/expenses/<int:expense_id>/delete', methods=['POST'])
@login_required
def delete_expense(expense_id):
	expense = Expense.query.get_or_404(expense_id)

	db.session.delete(expense)
	db.session.commit()
	flash('Expense deleted successfully', 'success')
	return redirect(url_for('expense.expenses'))