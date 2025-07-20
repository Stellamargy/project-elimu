from flask import Flask
from server.models import db,migrate,User,Role,Instructor,Parent,Student
from .config import Config
from .extension import bcrypt
#Instantiate a flask app instance
app=Flask(__name__)
#load configurations
app.config.from_object(Config)
#initialize the app with the extension
db.init_app(app)
migrate.init_app(db=db,app=app)
bcrypt.init_app(app)
# Test the application by running it and navigating to a particular route
@app.route('/')
def home():
    return "Flask application loading"