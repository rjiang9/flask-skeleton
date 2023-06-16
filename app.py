from SpecList import app, db
from SpecList.auth.models import User
from SpecList.category.models import Category
from SpecList.models import Spec

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Spec': Spec, 'Category':Category}

