from flask import Flask
from server.models import db

#Instantiate a flask app instance
app=Flask(__name__)

#initialize the app with the extension
db.init_app(app)

# Test the application by running it and navigating to a particular route
@app.route('/')
def home():
    return "Flask application loading"