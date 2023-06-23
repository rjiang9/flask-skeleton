from flask import Blueprint

assertion  = Blueprint('assertion', __name__, template_folder='templates')

from . import views
