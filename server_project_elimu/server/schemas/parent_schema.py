from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import EXCLUDE
from server.app import marshmallow
from server.models import Parent
from .user_schema import UserSchema

class ParentSchema(UserSchema):
    class Meta(UserSchema.Meta):
        model = Parent
        load_instance = True
        
        

    # user_id is set by backend; show in response only
    user_id = auto_field(dump_only=True)

   
