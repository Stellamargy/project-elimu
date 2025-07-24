from server.app import marshmallow
from marshmallow_sqlalchemy import auto_field
from marshmallow import validates, ValidationError,EXCLUDE
from marshmallow.validate import Email,Length
from server.models import User
import re
# data rules for user(base schema) inputs using marshmallow
class UserSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model=User
        load_instance=True
        include_fk=True
        unknown = EXCLUDE
        ordered = True
    

    id=auto_field(dump_only=True)
    # False on first registration , becomes active after first login .
    active=auto_field(load_default=False)
    email = auto_field(
    required=True,
    validate=[
        Email(error="Invalid email format."),
        Length(max=80, error="Email must be at most 80 characters.")
    ]
)

    #custom validation
   
    #phone number-include country code , only kenyans , length too
    @validates('phone')
    def validate_phone(self, value):
        phone_regex = r'^\+254\d{9}$'
        if not re.match(phone_regex, value):
            raise ValidationError("Phone number must be a valid Kenyan number (e.g., +2547XXXXXXXX).")
    #password
    #length -atleast 8
    #must have at least one lowercase
    #must have at least one special character
    #must have at leat one digit .
    #must have at least one uppercase
    @validates('password')
    def validate_password(self, value):
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'
        if not re.match(password_regex, value):
            raise ValidationError(
                "Password must be at least 8 characters long, include uppercase, lowercase, a digit, and a special character."
            )
    @validates('national_identification_number')
    def validate_national_id(self,value):
        national_id_regex=r'^\d{1,20}$'
        if not re.match(national_id_regex,value):
            raise ValidationError('National identification number is invalid-it should only contain only digits ,max characters is 20')
   

        






 