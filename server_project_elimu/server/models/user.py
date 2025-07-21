from .database import db
from sqlalchemy import func
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    #first name and last name are required fields and characters is less than / equal to 40
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    # National id should have characters less than / equal to 20
    national_identification_number = db.Column(db.String(20), unique=True)
    # Email should be a valid email address and a required field
    email = db.Column(db.String(80), nullable=False, unique=True)
    # Follow right pattern and include code -Only Kenyans are allowed
    phone = db.Column(db.String(15))
    #Strong password  and a required field
    password = db.Column(db.String(128), nullable=False)
    #Should be an integer and required
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    # will have default value at creating-POST
    active = db.Column(db.Boolean, nullable=False, default=False) 
     #Should be an integer and required
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    updated_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    #maybe implement a soft delete later
    # deleted_by= db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())
    

    # Relationships
    role = db.relationship('Role', back_populates='users')
    
    # Self-referential relationships
    creator = db.relationship('User', foreign_keys=[created_by], remote_side=[id])
    updater = db.relationship('User', foreign_keys=[updated_by], remote_side=[id])
    #later implementation
    # deleter = db.relationship('User', foreign_keys=[deleted_by], remote_side=[id])

    instructor = db.relationship('Instructor', uselist=False, back_populates='user')
    student = db.relationship('Student', uselist=False, back_populates='user')
    parent = db.relationship('Parent', uselist=False, back_populates='user')
