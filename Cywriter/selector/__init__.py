from flask import Blueprint

selector  = Blueprint('selector', __name__, template_folder='templates')

from . import views
