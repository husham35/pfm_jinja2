from flask import Flask, render_template
from flask_session import Session
from flask_migrate import Migrate
from .extensions import db, login_manager

# blueprints
from .auth import auth as auth_blueprint
from .budget import budget as budget_blueprint
from .expense import expense as expense_blueprint
from .main import main as main_blueprint

# models
from .models import User
from .budget.models import Budget
from .expense.models import Expense, ExpenseCategory, ExpenseCategoryItem


# , static_folder='static'
def create_app():
	app = Flask(__name__, static_url_path='/', static_folder='static')
	app.secret_key = 'your_secret_key'
	app.config['SESSION_TYPE'] = 'filesystem'
	app.config.from_object('config.Config')
	Session(app)

	# Initialize extensions
	db.init_app(app)
	# db.create_all()
	migrate = Migrate(app, db)
	login_manager.init_app(app)

	# User loader callback
	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))


	# Register blueprints
	app.register_blueprint(auth_blueprint)
	app.register_blueprint(budget_blueprint)
	app.register_blueprint(expense_blueprint)
	app.register_blueprint(main_blueprint)


	# error pages
	@app.errorhandler(404)
	def page_not_found(e):
		return render_template('404.html'), 404
	
	@app.errorhandler(500)
	def internal_server_error(e):
		return render_template('500.html'), 500

	return app
