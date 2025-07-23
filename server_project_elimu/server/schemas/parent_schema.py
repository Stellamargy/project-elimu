from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import EXCLUDE
from server.app import marshmallow
from server.models import Parent

class ParentSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Parent
        load_instance = True
        include_fk = True
        unknown = EXCLUDE
        

    # user_id is set by backend; show in response only
    user_id = auto_field(dump_only=True)

   
