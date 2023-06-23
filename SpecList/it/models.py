from .. import db

class It(db.Model):
    __tablename__ = 'it'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<It {}>'.format(self.name)
