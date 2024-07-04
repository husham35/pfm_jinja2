from flask import render_template, redirect, url_for, flash, session, request

from . import budget
from ..extensions import db
from .models import Budget
from .forms import CreateBudgetForm, UpdateBudgetForm

from flask_login import login_required, UserMixin, logout_user, current_user



@budget.route('/budgets', strict_slashes=False, methods=['GET'])
@budget.route('/budgets/<int:budget_id>', methods=['GET'])
@login_required
def budgets(budget_id=None):
	user_id = current_user.id
	# if request.method == 'POST':
	# 	if form.validate_on_submit():
	# 		budget = Budget
	# else:
	if budget_id:
		return render_template('budget/view.html', budget_id=budget_id)
	# else:
	return render_template('budget/index.html')


# @budget.route('/budget', methods=['GET'])
# @login_required
# def budget():
	
# 	user_id = current_user.id
# 	# if request.method == 'POST':
# 	# 	if form.validate_on_submit():
# 	# 		budget = Budget
# 	# else:

# 	return render_template('budget/view.html')


@budget.route('/create_budget', methods=['GET', 'POST'])
@login_required
def create_budget():
	# form = CreateBudgetForm()
	# user_id = current_user.id
	# if request.method == 'POST':
	# 	if form.validate_on_submit():
	# 		budget = Budget
	# else:

	return render_template('budget/create.html')



@budget.route('/update_budget', methods=['GET', 'POST'])
@login_required
def update_budget():
	form = CreateBudgetForm()
	user_id = current_user.id
	# if request.method == 'POST':
	# 	if form.validate_on_submit():
	# 		budget = Budget




	# else:

	return render_template('budget/update.html')


@budget.route('/delete_budget', methods=['GET', 'POST'])
@login_required
def delete_budget():
	form = CreateBudgetForm()
	user_id = current_user.id
	# if request.method == 'POST':
	# 	if form.validate_on_submit():
	# 		budget = Budget




	# else:

	return render_template('budget/index.html')