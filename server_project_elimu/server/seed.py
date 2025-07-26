from .app import app, bcrypt
from server.models import db, Role, User, Instructor, Parent, Student, Administrator
from faker import Faker
from sqlalchemy import text

fake = Faker()

def seed_roles():
    role_names = ['Administrator', 'Instructor', 'Parent', 'Student']
    for name in role_names:
        existing = Role.query.filter_by(role_name=name).first()
        if not existing:
            role = Role(role_name=name, description=f"{name} role")
            db.session.add(role)
    db.session.commit()
    print("Roles seeded.")

def seed_users():
    roles = {role.role_name: role for role in Role.query.all()}
    admin_role = roles.get("Administrator")

    if not admin_role:
        print(" Administrator role not found. Skipping admin user creation.")
        return

    if not User.query.filter_by(email="admin@example.com").first():
        admin = Administrator(
            first_name="System",
            last_name="Admin",
            national_identification_number="12345678901234",
            email="admin@example.com",
            phone="+254719529448",
            _password=bcrypt.generate_password_hash("StrongPass123!").decode("utf-8"),
            role_id=admin_role.id,
            # type="administrator",
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin user seeded.")
    else:
        print("Admin user already exists.")

if __name__ == "__main__":
    with app.app_context():
        # print("Dropping all tables...")
        # db.drop_all()

        # print(" Dropping alembic_version if exists...")
        # with db.engine.connect() as conn:
        #     conn.execute(text("DROP TABLE IF EXISTS alembic_version;"))
        #     conn.commit()

        print("🛠️ Creating tables...")
        db.create_all()

        seed_roles()
        seed_users()
        print("seeding successful")

        # print(" Database reset and seeded successfully.")



