from flask import Blueprint,request,jsonify
from server.models import User,Instructor,Parent,Student,Administrator,db,Role
from server.schemas import UserSchema,InstructorSchema,ParentSchema,StudentSchema,AdministratorSchema
from marshmallow import ValidationError
from server.app import bcrypt

#Create Blueprint
auth=Blueprint('auth',__name__,url_prefix='/auth')

#Route to add users
@auth.route('/register',methods=['POST'])
def add_admin():
    # get json data from request
    data=request.get_json()
    # validate if created _by and role_id exist in  table
    creator=User.query.get(data.get("created_by"))
    role=Role.query.get(data.get("role_id"))
    if not creator or not role:
         return jsonify({"error": "Creator or role does not exist"}), 404
    #check for existing user 
    existing_user_email=User.query.filter_by(email=data.get("email")).first()
    existing_user_national_id=User.query.filter_by(national_identification_number=data.get("national_identification_number")).first()
    if existing_user_email or existing_user_national_id:
        return jsonify({"error":"User already exist"}),409
    
    # Dynamic dispatch based on role
    user_class_map = {
        'administrator': (AdministratorSchema, Administrator),
        'instructor': (InstructorSchema, Instructor),
        'parent':(ParentSchema, Parent),
        'student':(StudentSchema, Student)
    }
    mapping = user_class_map.get(role.role_name.lower())
    if not mapping:
        return jsonify({"error": "Unsupported role for registration."}), 400

    schema_class, model_class = mapping


    try:
        model_instance = schema_class().load(data)  # validate + deserialize
        model_instance.password=data.get("_password")
        db.session.add(model_instance)
        db.session.commit()
        return jsonify({"message": f"{role.role_name.capitalize()} registered successfully."}), 201

       

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400


    
    
    
    



        


       

