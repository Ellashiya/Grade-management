from flask import Blueprint, render_template, flash, request, redirect, url_for, jsonify
from flask_login import current_user, login_required, login_user, logout_user
from guide_control.user_mgmt import User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from . import db
from db_model.models import Plans, GradesManage, SchoolGrades, MockGrades, Boards, Comments, Replys

guide_view = Blueprint('guide_view', __name__, static_folder="static", template_folder="templates")

#메인
@guide_view.route('/')
@guide_view.route('/main')
def main():
    return render_template("index.html")

#회원가입
@guide_view.route('/register')
def register():
    if request.method == "POST":
        # 데이터 분할
        name = request.form.get('name')
        nickname = request.form.get('nickname')
        age = request.form.get('age')
        email = request.form.get('email')
        id = request.form.get('id')
        password = request.form.get('password1')
        password_check = request.form.get('password_check')
        school = request.form.get('school')

        # 유효성 검사
        user = Users.query.filter_by(id=id).first()
        if user:
            flash('이미 존재하는 아이디입니다.',category='error')
        elif len(nickname) < 2 :
            flash('닉네임은 2자 이상입니다', category='error')
        elif password != password_check:
            flash('비밀번호가 서로 다릅니다', category='error')
        elif len(password) < 7:
            flash('비밀번호가 너무 짧습니다', category='error')
        else:
            # DB에 저장
            new_user = Users(name=name, 
                            nickname=nickname,
                            age=age,
                            email=email,
                            id=id, 
                            password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            # 자동 로그인
            login_user(new_user, remember=True)
            flash('회원가입 완료', category='success')

            return redirect(url_for('guide.main'))
    return render_template('register.html')

#로그인
@guide_view.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # 데이터 분할
        id = request.form.get('id')
        password = request.form.get('password1')

        # DB 탐색
        user = Users.query.filter_by(id=id).first()
        if user:
            if check_password_hash(user.password, password):
                flash('로그인 완료', category='success')
                login_user(user, remember=True)
                return redirect(url_for('guide.main'))
            else:
                flash('비밀번호가 다릅니다.', category='error')
        else:
            flash('해당 아이디가 존재하지 않습니다.', category='error')

    return render_template('login.html')

#로그아웃
@guide_view.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
	logout_user()
	return redirect(url_for('guide.login'))

#비밀번호 찾기
@guide_view.route('/password', methods=['GET', 'POST'])
def password():
    return render_template('password.html')

#플래너
@guide_view.route('/planner', methods=['GET', 'POST'])
@login_required
def planner():
    # Todo Item 생성
    if request.method == "POST":
        content = request.form.get('content')
        dodone = request.form.get('dodone')
        d_day = request.form.get('d_day')

        # 유효성 검사
        if len(content) < 1:
            flash("내용이 없습니다.", category = "error")
        elif len(content) > 50:
            flash("내용이 너무 깁니다. 50자 이내", category = "error")
        else :
            # DB에 저장
            new_plan = Plans(user_id=current_user.id, content=content, dodone=dodone, d_day=d_day, set_date=set_date)    
            db.session.add(new_plan)
            db.session.commit()

            flash("추가 완료", category="success")
            return redirect(url_for('guide.planner'))
    return render_template('layout-planner.html')

#플래너 Todolist Item 수정
@guide_view.route('/planner/update', methods=['PUT'])
@login_required
def planner_update():
    if request.method == "PUT":
        plan = request.get_json()
        plan_id = plan.get('planId')
        dodone = plan.get('dodone')
        d_day = plan.get('d_day')

        select_plan = Plans.query.get(plan_id)
        if select_plan:
            if select_plan.user_id == current_user.id : 
                select_plan.dodone = dodone
                select_plan.d_day = d_day
                db.session.commit()

        return jsonify({})

#플래너 Todolist Item 삭제
@guide_view.route('/planner/delete', methods=['POST'])
@login_required
def planner_delete():
    if request.method == "POST":
        plan = request.get_json()
        plan_id = plan.get('planId')

        # DB 확인
        select_plan = Plans.query.get(plan_id)
        if select_plan:
            if select_plan.user_id == current_user.id:
                db.session.delete(select_plan)
                db.session.commit()
                return jsonify({'result':True})

        return jsonify({'result':False})

#성적 관리
@guide_view.route('/grades', methods=['GET', 'POST'])
@login_required
def grades():
    return render_template('layout-grades.html')

#게시판
@guide_view.route('/board', methods=['GET', 'POST'])
@login_required
def board():
    return render_template('layout-board.html')

#게시판 글
@guide_view.route('/board/view', methods=['GET', 'POST'])
@login_required
def board_view():
    return render_template('layout-board-view.html')

#댓글 추가
@guide_view.route('/comment/add', methods=['GET', 'POST'])
@login_required
def comment_add():
    return render_template('/board/view')

#댓글 수정
@guide_view.route('/comment/update/<int:id>', methods=['GET', 'POST'])
@login_required
def comment_update():
    return render_template('/board/view')

#댓글 삭제
@guide_view.route('/comment/delete/<int:id>')
@login_required
def comment_delete():
    return render_template('/board/view')

#답글 추가
@guide_view.route('/reply/add', methods=['GET', 'POST'])
@login_required
def comment_add():
    return render_template('/board/view')

#답글 수정
@guide_view.route('/reply/update/<int:id>', methods=['GET', 'POST'])
@login_required
def reply_update():
    return render_template('/board/view')

#답글 삭제
@guide_view.route('/reply/delete/<int:id>')
@login_required
def reply_delete():
    return render_template('/board/view')