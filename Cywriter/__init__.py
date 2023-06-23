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
login.login_view = 'auth.login'

# blueprint for auth routes in our app
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .home import home as home_blueprint
app.register_blueprint(home_blueprint)

from .task import task as task_blueprint
app.register_blueprint(task_blueprint)

from .category import category as category_bp
app.register_blueprint(category_bp)

from .selector import selector as selector_blueprint
app.register_blueprint(selector_blueprint)

from .assertion import assertion as assertion_blueprint
app.register_blueprint(assertion_blueprint)

from .it import it as it_blueprint
app.register_blueprint(it_blueprint)


# from Todolist import routes
from Cywriter import routes
