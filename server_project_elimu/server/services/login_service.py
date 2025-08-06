from server.schemas import LoginSchema
from server.utilis import success_response, error_response, TokenManager
from server.models import User
from server.extension import bcrypt
from marshmallow import ValidationError
from flask import jsonify


class LoginService:

    @staticmethod
    def get_user_by_email(login_credentials):
        user = User.query.filter_by(email=login_credentials.get("email")).first()
        return user

    @staticmethod
    def is_password_valid(login_credentials, user):
        is_password_valid = bcrypt.check_password_hash(
            user._password, login_credentials.get("_password")
        )
        return is_password_valid

    @staticmethod
    def is_user_active(user):
        return user.active

    # log in method / logic
    @classmethod
    def login_user(cls, data):
        # Create a login_schema to validate and deserialize data (login request)
        login_schema = LoginSchema()
        try:
            # use login schema
            login_credentials = login_schema.load(data)
            # Get a user instance -filter by the email column
            user = LoginService.get_user_by_email(login_credentials)
            if not user:
                return error_response(
                    status="error", message="Wrong email or password", status_code=401
                )

            # If a valid user compare request password and hashed password
            password_valid = LoginService.is_password_valid(login_credentials, user)
            if not password_valid:
                return error_response(
                    status="error", message="Wrong email or password", status_code=401
                )
            is_user_active = LoginService.is_user_active(user)
            if not is_user_active:
                return error_response(
                    status="error", message="Account is inactive", status_code=403
                )

            token = TokenManager.create_token(user)
            return success_response(
                status="success",
                message="Logging in sucessful",
                status_code=200,
                data=token,
            )

            # return "Successful logged in "
        except ValidationError as err:
            return error_response(
                status="error",
                status_code=400,
                message="Invalid data",
                errors=err.messages,
            )
