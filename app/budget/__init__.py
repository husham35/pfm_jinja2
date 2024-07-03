from flask import Blueprint

budget = Blueprint('budget', __name__, template_folder='templates')

from . import routes
