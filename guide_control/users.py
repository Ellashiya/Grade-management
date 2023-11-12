from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from db_model.models import db

db = SQLAlchemy()

class Users(db.Model, UserMixin):
    id = db.Column(db.String(20), primary_key = True)
    password = db.Column(db.String(20), nullable = False)
    name = db.Column(db.String(10), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    nickname = db.Column(db.String(20),nullable = False, unique = True)
    email = db.Column(db.String(50), unique = True)
    school = db.Column(db.String(50))

    plans = db.relationship('Plans', backerf='plan')
    gradesmange = db.relationship('GradesMange', backerf='gradesmanage')
    schoolgrades = db.relationship('SchoolGrades', backerf='schoolgrade')
    mockgrades = db.relationship('MockGrades', backerf='mockgrade')
	boards = db.relationship('Boards', backref='board')
    comments = db.relationship('Comments', backref='comment')