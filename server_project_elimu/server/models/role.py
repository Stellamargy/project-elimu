from .database import db
from sqlalchemy import func
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.Text(100))
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    users = db.relationship('User', back_populates='role')