from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

app.config['CACHE_TYPE'] = "null" # Ray:Disable cache. Change "null" to "redis" when on production

db = SQLAlchemy(app)

migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'auth_bp.login'

# blueprint for auth routes in our app
from .auth import auth_bp
app.register_blueprint(auth_bp)

# blueprint for non-auth parts of app
from .home import home_bp
app.register_blueprint(home_bp)

from .spec import spec_bp
app.register_blueprint(spec_bp)

from .category import category_bp
app.register_blueprint(category_bp)

from .selector import selector_bp
app.register_blueprint(selector_bp)

from .assertion import assertion_bp
app.register_blueprint(assertion_bp)

from .step import step_bp
app.register_blueprint(step_bp)


# from Todolist import routes
from Cywriter import routes
