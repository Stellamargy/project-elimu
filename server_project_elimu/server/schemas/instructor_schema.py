from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import EXCLUDE
from server.app import marshmallow
from server.models import Instructor
from .user_schema import UserSchema

class InstructorSchema(UserSchema):
    class Meta(UserSchema.Meta):
        model = Instructor
        load_instance = True
        
        

   

    
