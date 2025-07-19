from .database import db
from sqlalchemy import func
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    national_identification_number = db.Column(db.String, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    phone = db.Column(db.String)
    password = db.Column(db.String, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    # Relationships
    role = db.relationship('Role', back_populates='users')
    # self-reference
    creator = db.relationship('User', remote_side=[id])
    instructor = db.relationship('Instructor', uselist=False, back_populates='user')
    student = db.relationship('Student', uselist=False, back_populates='user')
    parent = db.relationship('Parent', uselist=False, back_populates='user')
