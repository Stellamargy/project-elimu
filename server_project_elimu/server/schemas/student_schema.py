from server.app import marshmallow
from marshmallow_sqlalchemy import auto_field
from marshmallow import validates, ValidationError,EXCLUDE
from server.models import Student

class StudentSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model=Student
        load_instance=True
        include_fk=True
        unknown = EXCLUDE
        exclude = ("id",)

    user_id = auto_field(dump_only=True)


        
    