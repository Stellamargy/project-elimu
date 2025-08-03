from flask import Blueprint, request, jsonify
from server.models import User, Instructor, Parent, Student, Administrator, db, Role
from server.schemas import (
    UserSchema, InstructorSchema, ParentSchema, StudentSchema, AdministratorSchema
)
from marshmallow import ValidationError
from server.app import bcrypt
from server.services.user_service import UserService



auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/register', methods=['POST'])
def add_user():
    request_data = request.get_json()
    return UserService.register_user(request_data)

@auth.route('/login')
def login():
    login_credintials=request.get_json()
    

            


    










        


       

