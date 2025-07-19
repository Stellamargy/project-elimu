from flask import Flask

#Instantiate a flask app instance
app=Flask(__name__)

# Test the application by running it and navigating to a particular route
@app.route('/')
def home():
    return "Flask application loading"