from .database import db
from .user import User
from .instructor import Instructor
from sqlalchemy import CheckConstraint
class Administrator(User):
    __tablename__ = 'administrators'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    access_level = db.Column(db.String(100), nullable=False, default='supervisor')
    __table_args__ = (
    CheckConstraint(
        "access_level IN ('supervisor', 'system_admin')", name='access_level'
    ),
)
    __mapper_args__ = {
        'polymorphic_identity': 'administrator'
    }
