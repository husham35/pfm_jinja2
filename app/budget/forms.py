from flask_wtf import FlaskForm

from wtforms import StringField, FloatField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError


def date_not_earlier(form, field):
    start_date = form.start_date.data
    end_date = field.data
    if start_date and end_date and end_date < start_date:
        raise ValidationError('End Date cannot be earlier than Start Date')


class CreateBudgetForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired(), Length(min=2, max=200)])
	start_date = DateField('Start Date', validators=[DataRequired()], format='%d-%m-%Y')
	end_date = DateField('End Date', validators=[DataRequired(), date_not_earlier], format='%d-%m-%Y')
	limit = FloatField('Limit', validators=[DataRequired()])
	submit = SubmitField('Save')
     

class UpdateBudgetForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired(), Length(min=2, max=200)])
	start_date = DateField('Start Date', validators=[DataRequired()], format='%d-%m-%Y')
	end_date = DateField('End Date', validators=[DataRequired(), date_not_earlier], format='%d-%m-%Y')
	limit = FloatField('Limit', validators=[DataRequired()])
	submit = SubmitField('Update')


	