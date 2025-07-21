from server.app import marshmallow
from server.models import User
# data rules for user inputs using marshmallow
class UserSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model=User

 