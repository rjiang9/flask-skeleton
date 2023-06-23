from .. import db

class Assertion(db.Model):
    __tablename__ = 'assertion'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Assertion {}>'.format(self.name)
