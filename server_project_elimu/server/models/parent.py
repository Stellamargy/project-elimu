from .database import db
from sqlalchemy import func
class Parent(db.Model):
    __tablename__ = 'parents'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    user = db.relationship('User', back_populates='parent')