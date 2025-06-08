from . import db
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal = db.Column(db.String(10), nullable=False)
