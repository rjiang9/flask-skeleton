from flask import Blueprint

spec = Blueprint('spec', __name__, template_folder='templates')

from . import views
