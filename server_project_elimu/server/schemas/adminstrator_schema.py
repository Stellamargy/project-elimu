from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import EXCLUDE
from server.app import marshmallow
from server.models import Administrator
from .user_schema import UserSchema
from marshmallow import validate
from marshmallow.validate import Length


class AdministratorSchema(UserSchema):
    class Meta(UserSchema.Meta):
        model = Administrator
        load_instance = True

    access_level = auto_field(
    load_default='supervisor',
    validate=validate.OneOf(['supervisor', 'system_admin'], error='Invalid access level.')
)