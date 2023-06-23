from .. import db

class Selector(db.Model):
    __tablename__ = 'selector'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Selector {}>'.format(self.name)
