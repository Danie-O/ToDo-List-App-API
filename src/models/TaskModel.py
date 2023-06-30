from . import db
import datetime

from marshmallow import fields, Schema
# from .UserModel import UserSchema


class TaskModel(db.Model):
    """ 
    Todo List Task Model. 
    """

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.title = data.get('title')
        self.description = data.get('description')
        self.user_id = data.get('user_id')
        self.completed = data.get('completed')
        self.due_date = data.get('due_date')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        de.session.commit()
    
    @staticmethod
    def get_all_tasks():
        return TaskModel.query.all()
    
    @staticmethod
    def get_task_by_title(title):
        return TaskModel.query.get(title)

    def __repr__(self): 
        return '<id {}>'.format(self.id)


class TaskSchema(Schema):
    """
    Todo Task Schema

    Args:
        Schema (_type_): _description_
    """
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    owner_id = fields.Int(required=True)
    due_date = fields.Date(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)