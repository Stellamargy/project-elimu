from .database import db
from sqlalchemy import func
from server.extension import bcrypt
class User(db.Model):
    #table name 
    __tablename__ = 'users'
   #user table columns.
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    national_identification_number = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    phone = db.Column(db.String(15))
    _password = db.Column(db.String(128), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True) 
    # used by CTI to know the child table
    type=db.Column(db.String(100),nullable=False)
    #Removed this to add a default system user 
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    updated_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    #maybe implement a soft delete later
    # deleted_by= db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    created_at = db.Column(db.DateTime, nullable=False,default=func.now())
    updated_at = db.Column(db.DateTime,nullable=False,default=func.now(), onupdate=func.now())


    #SQLAlchemy polymorphic behaviour 
    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'user'  # default identity
    }

    

    # Relationships
    role = db.relationship('Role', back_populates='users')
    
    # Self-referential relationships
    creator = db.relationship('User', foreign_keys=[created_by], remote_side=[id])
    updater = db.relationship('User', foreign_keys=[updated_by], remote_side=[id])
    

    
    @property
    def password(self):
        raise AttributeError("Password is write-only.")

    @password.setter
    def password(self, plaintext_password):
        self._password = bcrypt.generate_password_hash(plaintext_password).decode("utf-8")

    