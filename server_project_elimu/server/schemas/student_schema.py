from server.app import marshmallow
from marshmallow_sqlalchemy import auto_field
from marshmallow import validates, ValidationError,EXCLUDE
from server.models import Student
from .user_schema import UserSchema

class StudentSchema(UserSchema):
    class Meta(UserSchema.Meta):
        model=Student
        load_instance=True
        
  


        
    