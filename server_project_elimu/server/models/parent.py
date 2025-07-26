from .database import db
from .user import User

class Parent(User):
    __tablename__ = 'parents'
    #one to one relationship in db level and enforces CTI
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    address = db.Column(db.Text)
    __mapper_args__ = {
        'polymorphic_identity': 'parent'
    }