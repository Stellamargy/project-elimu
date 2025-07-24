from .database import db

class Parent(db.Model):
    __tablename__ = 'parents'
    #one to one relationship in db level and enforces CTI
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    address = db.Column(db.Text)
    

    user = db.relationship('User', back_populates='parent')