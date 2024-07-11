import os

class Config:
	BASE_DIR = os.path.abspath(os.path.dirname(__file__))
	SECRET_KEY = 'MYSUPERSECRETKEY'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR ,'app/pfm_jinja2')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
