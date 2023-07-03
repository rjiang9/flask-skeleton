from flask import Blueprint

assertion_bp  = Blueprint('assertion_bp', __name__, template_folder='templates')

from . import views
