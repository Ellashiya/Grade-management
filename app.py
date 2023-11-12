from flask import Flask
from flask_login import LoginManager
from flask_cors import CORS
from guide_view import guide # (블루프린트)guide_view/guide.py 임포트
import os
from flask_sqlalchemy import SQLAlchemy
from os import path

# https 만 지원하는 기능을 http에서 테스트하기 위해 사용
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# 플라스크 앱 초기화
app = Flask(__name__, static_url_path='/static')
CORS(app)

# DB 경로 설정
db = SQLAlchemy()
DB_NAME = "database.db"

app.config['SECRET_KEY'] = 'load_management'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)
db.create_database(app)

# DB 파일 확인 및 생성
def create_database(app):
    if not path.exists(f'.{DB_NAME}'):
        db.create_all(app=app)

# flask-login 적용
login_manager = LoginManager()
login_manager.login_view = 'guide_view.guide.login'
login_manager.init_app(app)

# @login_manager.user_loader # 구현 필요
# def load_user(id):
#     return Users.query.get(id)

# 블루 프린트 적용
app.register_blueprint(guide.guide_view, url_prefix="")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='1114', debug=True) 
    # http://localhost:1114/guide/