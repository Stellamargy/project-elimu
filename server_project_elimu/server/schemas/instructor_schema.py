from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import EXCLUDE
from server.app import marshmallow
from server.models import Instructor

class InstructorSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Instructor
        load_instance = True
        include_fk = True
        unknown = EXCLUDE
        ordered = True

    # user_id is the primary key — set by backend only
    user_id = auto_field(dump_only=True)

    
