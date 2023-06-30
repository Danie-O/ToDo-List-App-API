from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# from .TaskModel import TaskModel, TaskSchema
# from .UserModel import UserModel, UserSchema

#  initialise database
db = SQLAlchemy()
bcrypt = Bcrypt()
