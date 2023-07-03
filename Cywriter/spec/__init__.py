from flask import Blueprint

spec_bp = Blueprint('spec_bp', __name__, template_folder='templates')

from . import views
