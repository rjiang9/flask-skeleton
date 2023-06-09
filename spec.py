from Core import app, db
from Core.models import Spec
from Core.auth.models import User
from Core.task.models import Category

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Spec': Spec, 'Category':Category}

