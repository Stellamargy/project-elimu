from .database import db
from .user import User

class Instructor(User):
    __tablename__ = 'instructors'
    #one to one relationship in db level and enforces CTI
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    employee_number = db.Column(db.String(20), nullable=False, unique=True)
    __mapper_args__ = {
        'polymorphic_identity': 'instructor'
    }

