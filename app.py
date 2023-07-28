from Cywriter import app, db
from Cywriter.auth.models import User
from Cywriter.spec.models import Spec
from Cywriter.category.models import Category
from Cywriter.selector.models import Selector
from Cywriter.assertion.models import Assertion
from Cywriter.step.models import Step

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Spec': Spec, 'Category': Category, 'Step': Step, 'Selector': Selector, 'Assertion': Assertion} # include sub apps

