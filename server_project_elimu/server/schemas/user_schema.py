from server.app import marshmallow
from marshmallow_sqlalchemy import auto_field
from marshmallow import validates, ValidationError,EXCLUDE,fields
from marshmallow.validate import Email,Length
from server.models import User
import re
# data rules/validations,serialization and deserialiation configuration for user entity  
class UserSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model=User
        load_instance=True
        include_fk=True
        unknown = EXCLUDE
        ordered = True
        exclude = ("created_at","updated_at")
    

    id=auto_field(dump_only=True)
    _password = auto_field(
        load_only=True,
        required=True,
        
    )
    email = auto_field(
    required=True,
    validate=[
        Email(error="Invalid email ."),
        Length(max=80, error="Email should be a maximum of 80 characters.")
    ])
    created_by=auto_field(required=True)
    type=auto_field(required=False)

    #custom validation / data rules 
   
    #phone number-only kenyans(use country code) are allowed to register, should be a valid kenyan number
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
    @validates('_password')
    def validate_password(self, value):
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'
        if not re.match(password_regex, value):
            raise ValidationError(
                "Password must be at least 8 characters long, " \
                "include uppercase, lowercase, a digit, and a special character."
            )
    @validates('national_identification_number')
    def validate_national_id(self,value):
        national_id_regex=r'^\d{1,20}$'
        if not re.match(national_id_regex,value):
            raise ValidationError('National identification number is invalid')
   
    
            






 