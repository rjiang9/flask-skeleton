from flask import Blueprint

step_bp  = Blueprint('step_bp', __name__, template_folder='templates')

from . import views
