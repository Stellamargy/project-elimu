from .database import db
from .user import User

class Student(User):
    __tablename__ = 'students'
    #Enforces one to one CTI integrity 
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    student_number = db.Column(db.String(20), nullable=False, unique=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'student'
    }
 
    

   