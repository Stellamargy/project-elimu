from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#create a db instance 
db=SQLAlchemy()
migrate=Migrate()