from flask import Blueprint

inventory = Blueprint('inventory', __name__, static_folder='static', template_folder='templates', url_prefix='/inventory')

from . import views