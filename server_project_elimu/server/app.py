from flask import Flask
from server.models import db,migrate,User,Role,Instructor,Parent,Student,Administrator
from .config import Config
from .extension import bcrypt,marshmallow
from server.controllers import auth

#Instantiate a flask app instance
app=Flask(__name__)

#load configurations
app.config.from_object(Config)

#integrate extension with app
db.init_app(app)
migrate.init_app(db=db,app=app)
bcrypt.init_app(app)
marshmallow.init_app(app)

#Register blueprints
app.register_blueprint(auth)
# Test the application by running it and navigating to a particular route
@app.route('/')
def home():
    return "Flask application loading"