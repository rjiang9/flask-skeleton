from Cywriter import db
from datetime import datetime

class Spec(db.Model):
    __tablename__ = 'spec'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    baseurl = db.Column(db.String(40))
    category = db.Column(db.String, db.ForeignKey('category.name'))
    funtionname = db.Column(db.String(40))

    loginrequired = db.Column(db.String(1))
    beforeaction = db.Column(db.String(40))
    postaction = db.Column(db.String(40))

    acct1 = db.Column(db.String(40))
    acct2 = db.Column(db.String(40))
    acct3 = db.Column(db.String(40))

    email1 = db.Column(db.String(40))
    email2 = db.Column(db.String(40))
    email3 = db.Column(db.String(40))

    prerequisites = db.Column(db.String(240))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Spec {}>'.format(self.name)

