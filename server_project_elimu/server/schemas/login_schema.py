from marshmallow import Schema, fields, validate, ValidationError,validates
import re
class LoginSchema(Schema):
    
    email=fields.Email(
        allow_none=False,
        required=True,
        validate=validate.Length(max=80,error="email should be a maximum of 80 characters"),
        error_messages={
            "required":"email is required",
            "email":"Invalid email",
            "null":"This field cannot be null"

        }
    )
    _password=fields.String(
        allow_none=False,
        required=True,
        validate=validate.Length(min=8,error="password should be atleast 8 characters"),
        error_messages={
            "invalid":"_password should be a string",
            "required":"_password is a required field",
            "null":"This field cannot be null"
        }
    )

    @validates('_password')
    def validate_password(self, value):
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'
        if not re.match(password_regex, value):
            raise ValidationError(
                "Password must be at least 8 characters long, " \
                "include uppercase, lowercase, a digit, and a special character."
            ) 
    