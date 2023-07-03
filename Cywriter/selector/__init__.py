from flask import Blueprint

selector_bp  = Blueprint('selector_bp', __name__, template_folder='templates')

from . import views
