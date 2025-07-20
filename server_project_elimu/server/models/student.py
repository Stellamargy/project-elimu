from .database import db

class Student(db.Model):
    __tablename__ = 'students'
    #one to one relationship in db level and enforces CTI
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    student_number = db.Column(db.String(20), nullable=False, unique=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    

    user = db.relationship('User', back_populates='student')