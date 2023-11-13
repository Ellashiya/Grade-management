from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def setup_db(app):
    '''db 테이블 생성'''
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()

class User(db.Model):
    id = db.Column(db.String(20), primary_key = True)
    password = db.Column(db.String(20), nullable = False)
    name = db.Column(db.String(10), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    nickname = db.Column(db.String(20), nullable = False, unique = True)
    email = db.Column(db.String(50), unique = True)
    school = db.Column(db.String(50))

    plans = db.relationship('Plans', backref='plan')
    gradesmange = db.relationship('GradesMange', backref='gradesmanage')
    schoolgrades = db.relationship('SchoolGrades', backref='schoolgrade')
    mockgrades = db.relationship('MockGrades', backref='mockgrade')
    boards = db.relationship('Boards', backref='board')
    comments = db.relationship('Comments', backref='comment')
    
class Plans(db.Model):
    plan_id = db.Column(db.Integer, primary_key = True)
    #user_id = db.Column(db.String(20), db.ForeignKey('users.id')) #오류
    content = db.Column(db.String(50))
    dodone= db.Column(db.String(4))
    d_day = db.Column(db.DateTime, default=datetime.utcnow)
    set_date = db.Column(db.DateTime, default=datetime.utcnow)

class GradesManage(db.Model):
    manage_id = db.Column(db.Integer, primary_key = True)
    # user_id = db.Column(db.String(20), db.ForeignKey('users.id'))
    # schoolgrade_id = db.Column(db.Integer, db.ForeignKey('schoolgrades.schoolgrade_id'))
    # mockgrade_id = db.Column(db.Integer, db.ForeignKey('mockgrades.mockgrade_id'))
    avr_school = db.Column(db.Float)
    avr_mock = db.Column(db.Float)

class SchoolGrades(db.Model):
    schoolgrade_id = db.Column(db.Integer, primary_key = True)
    # user_id = db.Column(db.String(20), db.ForeignKey('users.id'))
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
    # user_id = db.Column(db.String(20), db.ForeignKey('users.id'))
    grade = db.Column(db.Integer, nullable = False)
    year = db.Column(db.DateTime, default=datetime.year)
    month = db.Column(db.Integer, default=datetime.month)
    subject = db.Column(db.Integer, default = 0)
    score = db.Column(db.Integer, default = 0)
    rank = db.Column(db.String(6))

class Boards(db.Model):
    board_id = db.Column(db.Integer, primary_key = True)
    # user_id = db.Column(db.String(20), db.ForeignKey('users.id'))
    title = db.Column(db.String(50), nullable = False)
    content = db.Column(db.Text)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, default=datetime.utcnow)
    views = db.Column(db.Integer, default = 0)

    comments = db.relationship('Comments', backref='comment')

class Comments(db.Model):
    comment_id = db.Column(db.Integer, primary_key = True)
    # user_id = db.Column(db.String(20), db.ForeignKey('users.id'))
    # board_id = db.Column(db.Integer, db.ForeignKey('boards.board_id'))
    content = db.Column(db.Text)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    replys = db.relationship('Replys', backref='reply')

class Replys(db.Model):
    reply_id = db.Column(db.Integer, primary_key = True)
    # user_id = db.Column(db.String(20), db.ForeignKey('users.id'))
    # comment_id = db.Column(db.Integer, db.ForeignKey('comments.comment_id'))
    # board_id = db.Column(db.Integer, db.ForeignKey('boards.board_id'))
    content = db.Column(db.Text)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    