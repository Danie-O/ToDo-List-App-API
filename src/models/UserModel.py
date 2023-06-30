import datetime
from . import db
from ..app import bcrypt

from marshmallow import fields, Schema
from .TaskModel import TaskSchema


class UserModel(db.Model):
    """ 
    User Model. 
    """

    # define table name and attributes
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    tasks = db.relationship('TaskModel', backref='users', lazy=True)

    # class constructor
    def __init__(self, data):
        """ 
        UserModel constructor. 
        """
        self.name = data.get('name')
        self.email = data.get('email')
        self.password = self.generate_hash(data.get('password'))
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            if key == 'password':
                self.password = self.generate_hash(value)
            setattr(self, key, item)
            self.modified_at = datetime.datetime.utcnow()
            db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def generate_hash(self, password):
        return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")
   
    def check_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)
        
    @staticmethod
    def get_all_users():
        return UserModel.query.all()

    @staticmethod
    def get_one_user(name):
        return UserModel.query.get(name)

    def __repr__(self):
        return '<id {}>'.format(self.id) 


class UserSchema(Schema):
    """
    User Schema

    Args:
        Schema (_type_): _description_
    """
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    tasks = fields.Nested(TaskSchema, many=True)