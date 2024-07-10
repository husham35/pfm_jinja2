from flask import Blueprint

# , static_url_path=current_directory + '/app/', static_folder='static'
budget = Blueprint('budget', __name__, template_folder='templates')

from . import routes
# , static_folder='./static', static_url_path='/'