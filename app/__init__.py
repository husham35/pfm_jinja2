from flask import Flask
from flask_migrate import Migrate
from .extensions import db, login_manager
from .auth import auth as auth_blueprint
from .main import main as main_blueprint
from .models import User


def create_app():
	app = Flask(__name__)
	app.config.from_object('config.Config')

	# Initialize extensions
	db.init_app(app)
	migrate = Migrate(app, db)
	login_manager.init_app(app)

	# User loader callback
	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))


	# Register blueprints
	app.register_blueprint(auth_blueprint)
	app.register_blueprint(main_blueprint)

	return app
