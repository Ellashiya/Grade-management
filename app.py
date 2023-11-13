from flask import Flask, jsonify, request, render_template, make_response
from flask_login import LoginManager
from flask_cors import CORS
from guide_view import guide # (블루프린트)guide_view/guide.py 임포트
from guide_control.user_mgmt import User
from flask_sqlalchemy import SQLAlchemy
import os


# https 만 지원하는 기능을 http에서 테스트하기 위해 사용
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# 플라스크 앱 초기화
app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secret_key = 'guide'

# 블루 프린트 적용
app.register_blueprint(guide.guide_view, url_prefix='/guide')

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)

# db
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='1114', debug=True) 
    # http://localhost:1114/guide/