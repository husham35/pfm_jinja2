from flask import Flask
from .extensions import db, login_manager
from .auth import auth as auth_blueprint
from .main import main as main_blueprint


def create_app():
	app = Flask(__name__)
	app.config.from_object('config.Config')

	# Initialize extensions
	db.init_app(app)
	login_manager.init_app(app)


	# Register blueprints
	app.register_blueprint(auth_blueprint)
	app.register_blueprint(main_blueprint)

	return app
