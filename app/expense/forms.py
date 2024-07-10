from flask_wtf import FlaskForm

from ..budget.models import Budget
from .models import Expense, ExpenseCategory, ExpenseCategoryItem
from flask_login import current_user
from wtforms import StringField, FloatField, DateField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError


def date_not_earlier(form, field):
    start_date = form.start_date.data
    end_date = field.data
    if start_date and end_date and end_date < start_date:
        raise ValidationError('End Date cannot be earlier than Start Date')
      
class CreateExpenseForm(FlaskForm):
	amount = FloatField('Amount', validators=[DataRequired()])
	date = DateField('Date', validators=[DataRequired()], format='%Y-%m-%d')
	description = TextAreaField('Description', validators=[DataRequired()])
	budget_id = SelectField('Budget', validators=[DataRequired()])
	category_id = SelectField('Category', validators=[DataRequired()])
	category_item_id = SelectField('Category Item', validators=[DataRequired()])
	submit = SubmitField('Save')


	def __init__(self, *args, **kwargs):
		super(CreateExpenseForm, self).__init__(*args, **kwargs)
		if current_user.is_authenticated:
			self.budget_id.choices = [(int(option.id), option.name) for option in Budget.query.filter_by(user_id=current_user.id).all()]
			self.category_id.choices = [(int(option.id), option.name) for option in ExpenseCategory.query.filter_by(user_id=current_user.id).all()]
			self.category_item_id.choices = [(int(option.id), option.name) for option in ExpenseCategoryItem.query.filter_by(user_id=current_user.id).all()]
		else:
			self.budget_id.choices = []
			self.category_id.choices = []
			self.category_item_id.choices = []

class CreateExpenseCategoryForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	description = TextAreaField('Description', validators=[DataRequired()])
	submit = SubmitField('Save')
      

class CreateExpenseCategoryItemForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	description = TextAreaField('Description', validators=[DataRequired()])
	category_id = StringField('Category', validators=[DataRequired()])
	submit = SubmitField('Save')
     

# class UpdateBudgetForm(FlaskForm):
# 	name = StringField('Name', validators=[DataRequired(), Length(min=2, max=200)])
# 	start_date = DateField('Start Date', validators=[DataRequired()], format='%Y-%m-%d')
# 	end_date = DateField('End Date', validators=[DataRequired(), date_not_earlier], format='%Y-%m-%d')
# 	amount = FloatField('Amount', validators=[DataRequired()])
# 	submit = SubmitField('Update')


	