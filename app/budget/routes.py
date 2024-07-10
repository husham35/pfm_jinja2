from flask import render_template, redirect, url_for, flash, session, request

from . import budget
from ..extensions import db
from .models import Budget
from .forms import CreateBudgetForm, UpdateBudgetForm

from flask_login import login_required, UserMixin, logout_user, current_user


@budget.route('/budgets', strict_slashes=False, methods=['GET'])
@budget.route('/budgets/<int:budget_id>')
@login_required
def budgets(budget_id=None):
	user_id = current_user.id
	
	# get all budgets
	all_budgets = Budget.query.filter_by(user_id=user_id).all()

	if budget_id:
		single_budget = Budget.query.filter_by(id=budget_id).first()
		return render_template('budget/view.html', budget=single_budget)
	# else:
	return render_template('budget/index.html', budgets=all_budgets)


@budget.route('/budgets/create', methods=['GET', 'POST'])
@login_required
def create_budget():
	form = CreateBudgetForm()
	user_id = current_user.id
	if request.method == 'POST':
		if form.validate_on_submit():
			budget = Budget(
				name=form.name.data,
				start_date=form.start_date.data,
				end_date=form.end_date.data,
				amount=float(form.amount.data),
				user_id=user_id,
			)
			db.session.add(budget)
			db.session.commit()
			flash('Budget added successfully', 'success')
			return redirect(url_for('budget.budgets'))
		else:
			flash('Failed to save budget', 'warning')

	return render_template('budget/create.html', form=form)



@budget.route('/budgets/<int:budget_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_budget(budget_id):
	# user_id = current_user.id
	budget = Budget.query.get_or_404(budget_id)

	form = CreateBudgetForm(obj=budget)

	if request.method == 'POST':
		if form.validate_on_submit():

			form.populate_obj(budget)
			db.session.commit()
			flash('Budget updated successfully', 'success')
			return redirect(url_for('budget.budgets'))
		else:
			flash('Failed to update budget', 'warning')

	return render_template('budget/update.html', budget=budget, form=form)


@budget.route('/budgets/<int:budget_id>/delete', methods=['POST'])
@login_required
def delete_budget(budget_id):
	budget = Budget.query.get_or_404(budget_id)

	db.session.delete(budget)
	db.session.commit()
	flash('Budget deleted successfully', 'success')
	return redirect(url_for('budget.budgets'))