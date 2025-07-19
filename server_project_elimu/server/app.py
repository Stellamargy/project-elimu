from flask import Flask
from server.models import db
from .config import Config

#Instantiate a flask app instance
app=Flask(__name__)
#load configurations
app.config.from_object(Config)
#initialize the app with the extension
db.init_app(app)

# Test the application by running it and navigating to a particular route
@app.route('/')
def home():
    return "Flask application loading"