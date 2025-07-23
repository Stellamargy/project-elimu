from flask import Blueprint,request,jsonify
from server.models import User,Instructor,Parent,Student,db
from server.schemas import UserSchema,InstructorSchema,ParentSchema,StudentSchema
from marshmallow import ValidationError

#Create Blueprint
auth=Blueprint('auth',__name__,url_prefix='/auth')

#Route to add users
@auth.route('/register',methods=['POST'])
def add_user():
    # get json data from request
    data=request.get_json()
    user_schema =UserSchema()
    
    try:
        #use UserSchema to validate data
        user_data= user_schema.load(data.get('user'))
    except ValidationError as err:
        return jsonify({"error":err.messages}), 422
    #Create a user
    #Check if the user is unique
    if User.query.filter_by(email=user_data["email"]).first() or \
          User.query.filter_by(id=user_data["national_identification_number"]).first():
        return jsonify({"error":"User already exists"}),409
    new_user=User(**user_data)
    db.session.add(new_user)
    db.session.commit()

    # use role id to determine the child table
    role_id = user_data["role_id"]
    #Base on the role id insert data in the child table .
    if role_id == 3:  # Parent
        try:
            parent_schema = ParentSchema()
            parent_data = parent_schema.load(data.get("parent", {}))

            new_parent = Parent(user_id=new_user.id, **parent_data)
            db.session.add(new_parent)

        except ValidationError as err:
            db.session.rollback()
            return jsonify({"error": err.messages}), 422

    elif role_id == 2:  # Instructor
        try:
            instructor_schema = InstructorSchema()
            instructor_data = instructor_schema.load(data.get("instructor", {}))

            # Check if employee_number is unique
            if Instructor.query.filter_by(employee_number=instructor_data["employee_number"]).first():
                db.session.rollback()
                return jsonify({"error": "Employee number already exists"}), 409

            new_instructor = Instructor(user_id=new_user.id, **instructor_data)
            db.session.add(new_instructor)

        except ValidationError as err:
            db.session.rollback()
            return jsonify({"error": err.messages}), 422

    elif role_id == 4:  # Student
        try:
            student_schema = StudentSchema()
            student_data = student_schema.load(data.get("student", {}))

            # Check if student_number is unique
            if Student.query.filter_by(student_number=student_data["student_number"]).first():
                db.session.rollback()
                return jsonify({"error": "Student  already exists"}), 409

            new_student = Student(user_id=new_user.id, **student_data)
            db.session.add(new_student)

        except ValidationError as err:
            db.session.rollback()
            return jsonify({"error": err.messages}), 422

    # Save role-specific record
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201




        


       

