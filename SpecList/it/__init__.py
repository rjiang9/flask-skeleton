from flask import Blueprint

it  = Blueprint('it', __name__, template_folder='templates')

from . import views
