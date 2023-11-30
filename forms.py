from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, IntegerField, HiddenField, RadioField, SelectField
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
        
class GradesForm(FlaskForm):
    # 과목
    grade = StringField(
        "grade",
        validators=[
            DataRequired(message="과목은 필수입니다."), 
            Length(max=20, message="20글자 이내로 입력해주세요. ")
        ]
    )
    # 등수
    rank = StringField(
        "rank",
        validators=[
            DataRequired(message="등수는 필수입니다."), 
            Length(max=20, message="20글자 이내로 입력해주세요. ")
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
    # 학기
    semester = SelectField(
        "semester",
        validators=[
            DataRequired(message="학기는 필수입니다.")
        ]
    )
    # 등급
    rank = SelectField(
        "rank",
        validators=[
            DataRequired(message="등급은 필수입니다.")
        ]
    )
    # 학점제 유무
    is_rank = SelectField(
        "is_rank",
        validators=[
            DataRequired(message="학점제 유무는 필수입니다.")
        ]
    )
    
    # 연도
    year = SelectField(
        "year",
        validators=[
            DataRequired(message="학점제 유무는 필수입니다.")
        ]
    )
    # 월
    month = SelectField(
        "month",
        validators=[
            DataRequired(message="학점제 유무는 필수입니다.")
        ]
    )
    
    submit = SubmitField("성적 등록")

    