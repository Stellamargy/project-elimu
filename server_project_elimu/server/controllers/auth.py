from flask import Blueprint,request,jsonify
from server.models import User,Instructor,Parent,Student,Administrator,db,Role
from server.schemas import UserSchema,InstructorSchema,ParentSchema,StudentSchema,AdministratorSchema
from marshmallow import ValidationError
from server.app import bcrypt

#Create Blueprint
auth=Blueprint('auth',__name__,url_prefix='/auth')

#Route to add users
@auth.route('/register_admin',methods=['POST'])
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
    
    #manually assign type
    # data["type"]='administrator'
    try:
        admin_data = AdministratorSchema().load(data)  # validate + deserialize
        new_admin = Administrator(**admin_data)
        new_admin.password=data.get("password")
        
        db.session.add(new_admin)
        db.session.commit()

        return jsonify({"message": "Admin registered successfully."}), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400


    
    
    
    



        


       

