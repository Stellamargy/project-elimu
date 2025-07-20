from .app import app,bcrypt
from server.models import db, Role, User, Instructor, Parent, Student
from faker import Faker

fake = Faker()

def seed_roles():
    role_names = ['Admin', 'Instructor', 'Parent', 'Student']
    for name in role_names:
        existing = Role.query.filter_by(role_name=name).first()
        if not existing:
            role = Role(role_name=name, description=f"{name} role")
            db.session.add(role)
    db.session.commit()
    print("Roles seeded.")


def seed_users():
    roles = {role.role_name: role for role in Role.query.all()}

    # Create one admin
    if not User.query.filter_by(email="admin@example.com").first():
        admin = User(
            first_name="Admin",
            last_name="User",
            email="admin@example.com",
            #hash password
            password=bcrypt.generate_password_hash('hunter2'),  
            national_identification_number="00000001",
            role_id=roles["Admin"].id,
            active=True,
            created_by=1  # Self or system default user
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin user seeded.")

    # Create Students
    for _ in range(3):
        email = fake.unique.email()
        if not User.query.filter_by(email=email).first():
            student_user = User(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=email,
                password=bcrypt.generate_password_hash('hunter2'),
                national_identification_number=fake.unique.random_number(digits=8),
                role_id=roles["Student"].id,
                active=True,
                created_by=1
            )
            db.session.add(student_user)
            db.session.flush()  # Get the ID before commit
            student = Student(
                user_id=student_user.id,
                student_number=fake.unique.random_number(digits=5),
                date_of_birth=fake.date_of_birth(minimum_age=10, maximum_age=18)
            )
            db.session.add(student)
    db.session.commit()
    print("Students seeded.")

    # Create Instructors
    for _ in range(2):
        email = fake.unique.email()
        if not User.query.filter_by(email=email).first():
            instructor_user = User(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=email,
                password=bcrypt.generate_password_hash('hunter2'),
                national_identification_number=fake.unique.random_number(digits=8),
                role_id=roles["Instructor"].id,
                active=True,
                created_by=1
            )
            db.session.add(instructor_user)
            db.session.flush()
            instructor = Instructor(
                user_id=instructor_user.id,
                employee_number=fake.unique.random_number(digits=5)
            )
            db.session.add(instructor)
    db.session.commit()
    print("Instructors seeded.")

    # Create Parents
    for _ in range(2):
        email = fake.unique.email()
        if not User.query.filter_by(email=email).first():
            parent_user = User(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=email,
                password=bcrypt.generate_password_hash('hunter2'),
                national_identification_number=fake.unique.random_number(digits=8),
                role_id=roles["Parent"].id,
                active=True,
                created_by=1
            )
            db.session.add(parent_user)
            db.session.flush()
            parent = Parent(
                user_id=parent_user.id,
                address=fake.address()
            )
            db.session.add(parent)
    db.session.commit()
    print("Parents seeded.")


if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        seed_roles()
        seed_users()


