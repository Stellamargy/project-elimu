from .database import db
from sqlalchemy import func
class Student(db.Model):
    __tablename__ = 'students'
    #one to one relationship in db level and enforces CTI
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    student_number = db.Column(db.String(20), nullable=False, unique=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    user = db.relationship('User', back_populates='student')