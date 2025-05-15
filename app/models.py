from app import db

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(100), nullable=True)

#class User(db.model):
#    __tablename__ = 'users'
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(50), nullable=False)
#    password = db.Column(db.String(20),nullable=False)
#
#    task_id = db.Column(db.Integer, db.ForeignKey('tasks_id'), nullable=False)
