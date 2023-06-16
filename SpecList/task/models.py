from .. import db

class Category1(db.Model):
    __tablename__ = 'category1'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __repr__(self):
        return '<Category1 {}>'.format(self.name)
