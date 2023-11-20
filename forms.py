from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo

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
    