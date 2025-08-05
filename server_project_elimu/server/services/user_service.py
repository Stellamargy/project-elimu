from server.models import db,User,Student,Instructor,Role,Administrator,Parent
from server.schemas import (AdministratorSchema,
InstructorSchema,StudentSchema,ParentSchema,LoginSchema)
from server.utilis import error_response,success_response ,TokenManager
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from server.extension import bcrypt
from flask import jsonify



class UserService():
    user_class_map = {
        'administrator': (AdministratorSchema, Administrator),
        'instructor': (InstructorSchema, Instructor),
        'parent': (ParentSchema, Parent),
        'student': (StudentSchema, Student)
    }
    # let us start with data,let us make sure data passes certain rules 
  
    @staticmethod
    def validate_unique_fields(data):
        
        if User.query.filter_by(email=data.get("email")).first():
            return error_response(
                status="error",
                message="Email already exist",
                status_code=409

            )
        #unique national id - NB:allows null value
        if data.get("national_identification_number"):
            if User.query.filter_by(national_identification_number=data.get("national_identification_number")).first():
                return  error_response(
                status="error",
                message="National id  already exist",
                status_code=409

            )
        
        if Student.query.filter_by(student_number=data.get("student_number")).first():
            return error_response(
                status="error",
                message="Student number already exist",
                status_code=409
            )

        if Instructor.query.filter_by(employee_number=data.get("employee_number")).first():
            return error_response(
                status="error",
                message="Employee Number already exist",
                status_code=409
            )
    
    @staticmethod
    def is_creator_id_valid(data):
        if not User.query.get(data.get("created_by")):
            return error_response(
                status="error",
                message="Creator does not exist",
                status_code=404
            )
        
    @classmethod
    def register_user(cls, data):
        if not data.get("role_id"):
            return error_response(
                status="error",
                message="Role id is required",
                status_code=400
            )

        role = Role.query.get(data.get("role_id"))
        if not role:
            return error_response(
                status="error",
                message="Invalid role_id",
                status_code=400
            )

        role_name = role.role_name.lower()
        if role_name not in cls.user_class_map:
            return error_response(
                status="error",
                message="Role not supported",
                status_code=404
            )

        schema_class, model_class = cls.user_class_map.get(role_name)

        try:
            model_instance = schema_class().load(data)

            result = cls.validate_unique_fields(data)
            if result is not None:
                return result

            result = cls.is_creator_id_valid(data)
            if result is not None:
                return result

            model_instance.set_password(data.get("_password"))
            db.session.add(model_instance)
            db.session.commit()

            return success_response(
                status="success",
                message=f"{model_instance.type} created successfully",
                data=schema_class().dump(model_instance),
                status_code=201
            )

        except ValidationError as err:
            return error_response(
                status="error",
                message="Invalid input data. Please check the fields and try again.",
                status_code=400,
                errors=err.messages
            )

        except IntegrityError as err:
            db.session.rollback()
            return error_response(
                status="error",
                message="A database integrity error occurred. Possibly due to duplicate or invalid values.",
                status_code=409
            )

        except SQLAlchemyError as err:
            db.session.rollback()
            return error_response(
                status="error",
                message="A database error occurred.",
                status_code=500
            )

    # log in
    @classmethod
    def login_user(cls,data):
        # get login credentials ,validate input before proceeding to compare .
        login_schema=LoginSchema()
        try:
            login_credentials=login_schema.load(data)
            # Do db comparison 
            user=User.query.filter_by(email=login_credentials.get("email")).first()
            if not user:
                return error_response(
                    status="error",
                    message="Wrong email or password",
                    status_code=401
                    )
            is_password_valid=bcrypt.check_password_hash(
                user._password,
                login_credentials.get("_password"))
            if not is_password_valid:
                return error_response(
                    status="error",
                    message="Wrong email or password",
                    status_code=401
                )
            #check if the user is active
            if not user.active:
                return error_response(
                    status="error",
                    message="Account is inactive",
                    status_code=403
                )
            token =TokenManager.create_token(user)
            return success_response(
                status="sucess",
                message="Logging in sucessful",
                status_code=200,
                data=token
            )  
        
            # return "Successful logged in "
        except ValidationError as err:
            return error_response(
                status="error",
                status_code=400,
                message="Invalid data",
                errors=err.messages
            )
        


        


        
            

            