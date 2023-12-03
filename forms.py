from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, IntegerField, HiddenField, RadioField, SelectField, FormField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from datetime import datetime

class UserForm(FlaskForm):
    # 아이디
    id = StringField(
        "id",
        validators=[
            DataRequired(message="아이디는 필수입니다."), 
            Length(max=20, message="20글자 이내로 입력해주세요. ")
        ]
    )
    # 비밀번호
    password = PasswordField(
        "password",
        validators=[
            DataRequired(message="비밀번호는 필수입니다."), 
            Length(max=20, message="20글자 이내로 입력해주세요. "),
            EqualTo('password_confirm')
        ]
    )
    # 비밀번호 확인
    password_confirm = PasswordField(
        "password_confirm",
        validators=[
            DataRequired(message="비밀번호 확인은 필수입니다."), 
            Length(max=20, message="20글자 이내로 입력해주세요. "), 
        ]
    )
    # 이름
    name = StringField(
        "name",
        validators=[
            DataRequired(message="사용자명은 필수입니다."),
            Length(max=10, message="10글자 이내로 입력해주세요. ")
        ]
    )
    # 나이
    age = IntegerField(
        "age",
        validators=[
            DataRequired(message="나이는 필수입니다.")
        ]
    )
    # 닉네임
    nickname = StringField(
        "nickname",
        validators=[
            DataRequired(message="닉네임은 필수입니다."),
            Length(max=10, message="20글자 이내로 입력해주세요. ")
        ]
    )
    # 이메일
    email = StringField(
        "email",
        validators=[
            DataRequired(message="메일 주소는 필수입니다."),
            Email(message="메일 주소의 형식으로 입력해 주세요.")
        ]
    )
    # 학교
    school = StringField(
        "school",
        validators=[
            DataRequired(message="학교 이름은 필수입니다."),
            Length(max=50, message="50글자 이내로 입력해주세요. ")
        ]
    )
    
    submit = SubmitField("신규 등록")
    
class LoginForm(FlaskForm):
    # 아이디
    id = StringField(
        "id",
        validators=[
            DataRequired(message="아이디는 필수입니다."), 
            Length(max=20, message="20글자 이내로 입력해주세요. ")
        ]
    )
    # 비밀번호
    password = PasswordField(
        "password",
        validators=[
            DataRequired(message="비밀번호는 필수입니다.")
        ]
    )

class PlannerForm(FlaskForm):
    # 내용
    content = StringField(
        "content",
        validators=[
            DataRequired(message="내용을 입력해주세요."), 
            Length(max=50, message="50글자 이내로 입력해주세요. ")
        ]
    )
    # 할일/한일 구분
    dodone = RadioField(
        "dodone",
        choices=[('do','do'),('done','done')]
    )
    # 등록일
    set_date = HiddenField(
        "set_date",
        validators=[
            DataRequired(),
        ]
    )

    submit = SubmitField("할일/한일 등록")

    def validate_set_date(self, field):
        cleaned_date_string = field.data.replace('(한국 표준시)', '').strip()
        parsed_date = datetime.strptime(cleaned_date_string, '%a %b %d %Y %H:%M:%S %Z%z')
        field.data = parsed_date
        
        
class SchoolGradeForm(FlaskForm):
    # 학기
    semester = SelectField(
        "semester",
        choices=[('2013학년도 1학기', '2013학년도 1학기'), ('2013학년도 2학기', '2013학년도 2학기')]
    )
    # 과목
    grade = StringField(
        "grade",
        validators=[
            DataRequired(message="과목은 필수입니다."), 
            Length(max=20, message="20글자 이내로 입력해주세요. ")
        ]
    )
    # 등수
    schoolrank = StringField(
        "schoolrank",
        validators=[
            DataRequired(message="등수는 필수입니다."), 
            Length(max=20, message="20글자 이내로 입력해주세요. ")
        ]
    )
    # 등급
    rank = SelectField(
        "rank",
        choices = [
            ('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), 
            ('B', 'B'), ('C+', 'C+'), ('C', 'C'), 
            ('D+', 'D+'), ('D', 'D'), ('F', 'F'), 
            ('P', 'P'), ('U', 'U')
            ]
    )
    # 학점제 유무
    is_rank = SelectField(
        "is_rank",
        choices=[('O', 'O'), ('X', 'X')]
    )
    # 점수
    score = StringField(
        "score",
        validators=[
            DataRequired(message="점수는 필수입니다."), 
            Length(max=20, message="20글자 이내로 입력해주세요. ")
        ]
    )
    submit = SubmitField("중간고사 성적 등록")
    
class FinalGradeForm(FlaskForm):
    # 학기
    semester = SelectField(
        "semester",
        choices=[('2013학년도 1학기', '2013학년도 1학기'), ('2013학년도 2학기', '2013학년도 2학기')]
    )
    # 과목
    grade = StringField(
        "grade",
        validators=[
            DataRequired(message="과목은 필수입니다."), 
            Length(max=20, message="20글자 이내로 입력해주세요. ")
        ]
    )
    # 등수
    schoolrank = StringField(
        "schoolrank",
        validators=[
            DataRequired(message="등수는 필수입니다."), 
            Length(max=20, message="20글자 이내로 입력해주세요. ")
        ]
    )
    # 등급
    rank = SelectField(
        "rank",
        choices = [
            ('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), 
            ('B', 'B'), ('C+', 'C+'), ('C', 'C'), 
            ('D+', 'D+'), ('D', 'D'), ('F', 'F'), 
            ('P', 'P'), ('U', 'U')
            ]
    )
    # 학점제 유무
    is_rank = SelectField(
        "is_rank",
        choices=[('O', 'O'), ('X', 'X')]
    )
    # 점수
    score = StringField(
        "score",
        validators=[
            DataRequired(message="점수는 필수입니다."), 
            Length(max=20, message="20글자 이내로 입력해주세요. ")
        ]
    )
    submit = SubmitField("기말고사 성적 등록")
    
class MockGradeFrom(FlaskForm):
    # 연도
    year = SelectField(
        "year",
        choices=[('2013년', '2013년'), ('2014년', '2014년')]
    )
    # 월
    month = SelectField(
        "month",
        choices = [
            ('3월', '3월'), ('5월', '5월'), ('6월', '6월'),
            ('7월', '7월'), ('9월', '9월'), ('10월', '10월'),
            ('11월', '11월'), ('12월', '12월')
            ]
    )
    # 과목
    grade = StringField(
        "grade",
        validators=[
            DataRequired(message="과목은 필수입니다."), 
            Length(max=20, message="20글자 이내로 입력해주세요. ")
        ]
    )
    # 등급
    rank = SelectField(
        "rank",
        choices = [
            ('1', '1'), ('2', '2'), ('3', '3'),
            ('4', '4'), ('5', '5'), ('6', '6'),
            ('7', '7'), ('8', '8'), ('9', '9')
            ]
    )
    # 점수
    score = StringField(
        "score",
        validators=[
            DataRequired(message="점수는 필수입니다."), 
            Length(max=20, message="20글자 이내로 입력해주세요. ")
        ]
    )
    submit = SubmitField("모의고사 성적 등록")
    
    

    