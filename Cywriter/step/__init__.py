from flask import Blueprint

step  = Blueprint('step', __name__, template_folder='templates')

from . import views
