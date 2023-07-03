from flask import Blueprint

category_bp  = Blueprint('category_bp', __name__, template_folder='templates')

from . import views
