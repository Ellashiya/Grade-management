from flask import Flask, jsonify, request, render_template, make_response
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from guide_view import guide # (블루프린트)guide_view/guide.py 임포트
import os

# https 만 지원하는 기능을 http에서 테스트하기 위해 사용
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secret_key = 'load_management'

app.register_blueprint(guide.guide_app, url_prefix='/guide') # 블루프린트 등록
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'

# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

# 로그인하지 않은 유저가 허용되지 않은 부분에 접근할 경우
@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401) 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='1114') 
    # http://localhost:1114/guide/test