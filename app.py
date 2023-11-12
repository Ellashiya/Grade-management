from flask import Flask, jsonify, request, render_template, make_response
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from db_model.models import db
from guide_view import guide # (블루프린트)guide_view/guide.py 임포트
import os

# https 만 지원하는 기능을 http에서 테스트하기 위해 사용
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')
CORS(app)

#현재 있는 파일의 디렉토리 절대 경로
basdir = os.path.abspath(os.path.dirname(__file__))
#위 경로에 db파일 생성
dbfile = os.path.join(basdir, 'db.sqlite')

#사용할 DB URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
#Commint 실행(DB 반영)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#수정사항에 대한 TRACK
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#SECRET_Key
app.config['SECRET_KEY'] = 'load_management'

db.init_app(app)
db.app = app
db.create_all()

app.register_blueprint(guide.guide_view, url_prefix="")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'

# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

# 로그인하지 않은 유저가 허용되지 않은 부분에 접근할 경우
#@login_manager.unauthorized_handler
#def unauthorized():
#    return make_response(jsonify(success=False), 401) 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='1114', debug=True) 
    # http://localhost:1114/guide/