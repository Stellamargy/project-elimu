from .database import db
from sqlalchemy import func
class Instructor(db.Model):
    __tablename__ = 'instructors'
    #one to one relationship in db level and enforces CTI
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    employee_number = db.Column(db.String(20), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    user = db.relationship('User', back_populates='instructor')
