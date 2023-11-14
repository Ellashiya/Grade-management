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
    '''사용자(아이디, 비밀번호, 이름, 나이, 닉네임, 이메일, 학교)'''
    id = db.Column(db.String(20), primary_key = True)
    password = db.Column(db.String(20), nullable = False)
    name = db.Column(db.String(10), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    nickname = db.Column(db.String(20), nullable = False, unique = True)
    email = db.Column(db.String(50), unique = True)
    school = db.Column(db.String(50))

    # relationship
    plans = db.relationship('Plans', backref='plan')
    gradesmange = db.relationship('GradesMange', backref='gradesmanage')
    schoolgrades = db.relationship('SchoolGrades', backref='schoolgrade')
    mockgrades = db.relationship('MockGrades', backref='mockgrade')
    boards = db.relationship('Boards', backref='board')
    comments = db.relationship('Comments', backref='comment')
    
class Plans(db.Model):
    '''플래너(플래너 아이디, 사용자 아이디, 내용, 할일/한일, D-day 설정일, 등록일)'''
    plan_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(20), db.ForeignKey('User.id')) 
    content = db.Column(db.String(50))
    dodone= db.Column(db.String(4))
    d_day = db.Column(db.DateTime, default=datetime.utcnow)
    set_date = db.Column(db.DateTime, default=datetime.utcnow)

class GradesManage(db.Model):
    '''성적 관리(관리 아이디, 사용자 아이디, 내신 성적 아이디, 모의고사 성적 아이디, 내신 성적 평균, 모의고사 성적 평균)'''
    manage_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(20), db.ForeignKey('User.id'))
    schoolgrade_id = db.Column(db.Integer, db.ForeignKey('SchoolGrades.schoolgrade_id'))
    mockgrade_id = db.Column(db.Integer, db.ForeignKey('MockGrades.mockgrade_id'))
    avr_school = db.Column(db.Float)
    avr_mock = db.Column(db.Float)

class SchoolGrades(db.Model):
    '''내신 성적(내신 성적 아이디, 사용자 아이디, 학년, 연도, 학기, 중간고사 유무, 과목, 점수, 등급, 교내 등수, 교내 학생수, 등급제 유무)'''
    schoolgrade_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(20), db.ForeignKey('User.id'))
    grade = db.Column(db.Integer, nullable = False)
    year = db.Column(db.DateTime, default=datetime.year)
    semester = db.Column(db.Integer, default=1)
    ismidterm = db.Column(db.String(3), default='Yes')
    subject = db.Column(db.String(20), nullable = False)
    score = db.Column(db.Integer, default = 0)
    rank = db.Column(db.String(6))
    schoolrank = db.Column(db.Integer)
    student_num = db.Column(db.Integer)
    isRank = db.Column(db.String(3), default = 'Yes')

class MockGrades(db.Model):
    '''모의고사 성적(모의고사 성적 아이디, 사용자 아이디, 학년, 연도, 월, 과목, 점수, 등급)'''
    mockgrade_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(20), db.ForeignKey('User.id'))
    grade = db.Column(db.Integer, nullable = False)
    year = db.Column(db.DateTime, default=datetime.year)
    month = db.Column(db.Integer, default=datetime.month)
    subject = db.Column(db.String(20))
    score = db.Column(db.Integer, default = 0)
    rank = db.Column(db.String(6))

class Boards(db.Model):
    '''게시글(게시글 아이디, 사용자 아이디, 제목, 내용, 등록일, 수정일, 조회수)'''
    board_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(20), db.ForeignKey('User.id'))
    title = db.Column(db.String(50), nullable = False)
    content = db.Column(db.Text)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, default=datetime.utcnow)
    views = db.Column(db.Integer, default = 0)
    
    # relationship
    comments = db.relationship('Comments', backref='comment')

class Comments(db.Model):
    '''댓글(댓글 아이디, 사용자 아이디, 게시글 아이디, 내용, 등록일, 수정일)'''
    comment_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(20), db.ForeignKey('User.id'))
    board_id = db.Column(db.Integer, db.ForeignKey('Boards.board_id'))
    content = db.Column(db.Text)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # relationship
    replys = db.relationship('Replys', backref='reply')

class Replys(db.Model):
    '''답글(답글 아이디, 사용자 아이디, 상위 댓글 아이디, 게시글 아이디, 내용, 등록일, 수정일)'''
    reply_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(20), db.ForeignKey('User.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('Comments.comment_id'))
    board_id = db.Column(db.Integer, db.ForeignKey('Boards.board_id'))
    content = db.Column(db.Text)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    