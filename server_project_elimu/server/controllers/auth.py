from flask import Blueprint, request, jsonify
from server.models import User, Instructor, Parent, Student, Administrator, db, Role
from server.schemas import (
    UserSchema, InstructorSchema, ParentSchema, StudentSchema, AdministratorSchema
)
from marshmallow import ValidationError
from server.extension import bcrypt
from server.services import UserService,LoginService
from server.utilis import error_response



auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/register', methods=['POST'])
def add_user():
    request_data = request.get_json()
    return UserService.register_user(request_data)

@auth.route('/login',methods=['POST'])
def login():
    # get request json from request object
    login_credentials=request.get_json()
    # If no request dict
    if not login_credentials:
        return error_response(
            status="error",
            message="Missing request data",
            status_code=400
        )
    return LoginService.login_user(login_credentials)
    

        
   


            


    










        


       

