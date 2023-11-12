from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Users(db.Model, UserMixin):
    id = db.Column(db.String(20), primary_key = True)
    pw = db.Column(db.String(20), nullable = False)
    name = db.Column(db.String(10), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    nickname = db.Column(db.String(20),nullable = False, unique = True)
    email = db.Column(db.String(50), unique = True)
    school = db.Column(db.String(50))

    plans = db.relationship('Plans', backerf='plan')
    schoolgrades = db.relationship('SchoolGrades', backerf='schoolgrade')
    mockgrades = db.relationship('MockGrades', backerf='mockgrade')
	boards = db.relationship('Boards', backref='board')
    comments = db.relationship('Comments', backref='comment')

class Plans(db.Model):
    plan_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(20), db.ForeignKey('users.id'))
    do_content = db.Column(db.String(50))
    done_content = db.Column(db.String(50))
    d_day = db.Column(db.DateTime, default=datetime.utcnow)

class GradesManage(db.Model):
    

class SchoolGrades(db.Model):
    schoolgrade_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(20), db.ForeignKey('users.id'))
    grade = db.Column(db.Integer, nullable = False)
    year = db.Column(db.DateTime, default=datetime.year)
    semester = db.Column(db.Integer, default=1)
    ismidterm = db.Column(db.String(3), default='Yes')
    subject = db.Column(db.Integer, default = 0)
    score = db.Column(db.Integer, default = 0)
    rank = db.Column(db.String(6))
    schoolrank = db.Column(db.Integer)
    student_num = db.Column(db.Integer)
    isRank = db.Column(db.String(3), default = 'Yes')

class MockGrades(db.Model):
    mockgrade_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(20), db.ForeignKey('users.id'))
    grade = db.Column(db.Integer, nullable = False)
    year = db.Column(db.DateTime, default=datetime.year)
    month = db.Column(db.Integer, default=datetime.month)
    subject = db.Column(db.Integer, default = 0)
    score = db.Column(db.Integer, default = 0)
    rank = db.Column(db.String(6))

class Boards(db.Model):
    board_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(20), db.ForeignKey('users.id'))
    title = db.Column(db.String(50), nullable = False)
    content = db.Column(db.Text)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, default=datetime.utcnow)
    views = db.Column(db.Integer, default = 0)

    comments = db.relationship('Comments', backref='comment')

class Comments(db.Model):
    comment_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(20), db.ForeignKey('users.id'))
    board_id = db.Column(db.Integer, db.ForeignKey('boards.board_id'))
    content = db.Column(db.Text)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, default=datetime.utcnow)

    replys = db.relationship('Replys', backref='reply')

class Replys(db.Model):
    reply_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(20), db.ForeignKey('users.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.comment_id'))
    board_id = db.Column(db.Integer, db.ForeignKey('boards.board_id'))
    content = db.Column(db.Text)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, default=datetime.utcnow)