from flask import Flask, Blueprint, request, render_template, flash, redirect, url_for, session, jsonify
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from db_model.models import db, User, Plans
from datetime import datetime
from forms import UserForm, LoginForm, PlannerForm, SchoolGradeForm, MockGradeFrom, FinalGradeForm
import json

guide_view = Blueprint('guide_view', __name__, url_prefix='/')

@guide_view.route('/')
def index():
    return render_template('index.html')

@guide_view.route('/planner', methods=['GET', 'POST'])
def planner():
    current_date = datetime.now()
    form = PlannerForm()

    todolist = Plans.query.filter_by(user_id=current_user.id).all()

    if form.validate_on_submit() and request.method == 'POST':
        new_plan = Plans(
            user_id = current_user.id,
            content = form.content.data,
            dodone = form.dodone.data,
            set_date = form.set_date.data
        )
        db.session.add(new_plan)
        db.session.commit()
        return redirect(url_for('guide_view.planner'))
    
    return render_template('layout-planner.html', current_date=current_date, form=form, todolist=todolist)

@guide_view.route('/planner/update', methods=['POST'])
@login_required
def planner_update():
    plan_id = request.form.get('plan_id')
    d_day = request.form.get('d_day')
    select_plan = Plans.query.get(plan_id)

    if select_plan and d_day is not None:
        select_plan.d_day = datetime.strptime(d_day, '%Y-%m-%d')
        db.session.commit()

    return redirect(url_for('guide_view.planner'))

# @guide_view.route('/planner/update/checkbox', methods=['POST'])
# @login_required
# def planner_update_checkbox():
#     plan_id = request.form.get('plan_id')
#     dodone = request.form.get('dodone')

#     if plan_id and dodone is not None:
#         select_plan = Plans.query.get(plan_id)
#         if select_plan:
#             select_plan.dodone = dodone
#             db.session.commit()

#     return redirect(url_for('guide_view.planner'))
    
@guide_view.route('/planner/delete', methods=['POST'])
@login_required
def planner_delete():
    plan_id = request.form.get('plan_id')
    select_plan = Plans.query.get(plan_id)

    if select_plan:
        db.session.delete(select_plan)
        db.session.commit()

    return redirect(url_for('guide_view.planner'))
    
    
@guide_view.route('/grades')
def grades():
    midterm_form = SchoolGradeForm()
    f_form = FinalGradeForm()
    mock_form = MockGradeFrom()
    rate = 10
    return render_template('layout-grades.html',rate=rate, midterm_form=midterm_form, mock_form=mock_form, f_form=f_form)

# 내신 성적 추가 - 중간고사
@guide_view.route('/grades/school/midterm', methods=['POST'])
@login_required
def grades_midterm():
    midterm_form = SchoolGradeForm()
    f_form = FinalGradeForm()
    mock_form = MockGradeFrom()
    rate = 10
    
    if midterm_form.validate_on_submit():
        print('중간고사 추가')
    else:
        print(midterm_form.errors)
    
    return render_template('layout-grades.html',rate=rate, midterm_form=midterm_form, mock_form=mock_form, f_form=f_form)

# 내신 성적 추가 - 기말고사
@guide_view.route('/grades/school/final', methods=['POST'])
@login_required
def grades_final():
    midterm_form = SchoolGradeForm()
    f_form = FinalGradeForm()
    mock_form = MockGradeFrom()
    rate = 10
    
    if f_form.validate_on_submit():
        print('기말고사 추가')
    else:
        print(f_form.errors)
    
    return render_template('layout-grades.html',rate=rate, midterm_form=midterm_form, mock_form=mock_form, f_form=f_form)

# 모의고사 성적 추가
@guide_view.route('/grades/mock', methods=['POST'])
@login_required
def grades_mock():
    midterm_form = SchoolGradeForm()
    f_form = FinalGradeForm()
    mock_form = MockGradeFrom()
    rate = 10
    
    if mock_form.validate_on_submit():
        print('모의고사 추가')
    else:
        print(mock_form.errors)
    
    return render_template('layout-grades.html',rate=rate, midterm_form=midterm_form, mock_form=mock_form, f_form=f_form)

@guide_view.route('/board')
def board():
    return render_template('layout-board.html')

@guide_view.route('/login', methods=['GET', 'POST'])  
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(id=form.id.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            login_user(user)
            return redirect(url_for('guide_view.index'))
        flash(error)
    return render_template('login.html', form=form)

@guide_view.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
	logout_user()
	return redirect(url_for('guide_view.index'))

@guide_view.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit() and request.method == 'POST':
        user = User.query.filter_by(id=form.id.data).first()
        if not user: # 아이디가 존재하지 않을 경우 추가
            hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
            user = User(
                id = form.id.data,
                password = hashed_password,
                name = form.name.data,
                age = form.age.data,
                nickname = form.nickname.data,
                email = form.email.data,
                school = form.school.data
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('guide_view.index'))
        else:
            flash('이미 존재하는 사용자입니다.') 
              
    return render_template("register.html", form=form)

# #비밀번호 찾기
# @guide_view.route('/password', methods=['GET', 'POST'])
# def password():
#     return render_template('password.html')


# #게시판
# @guide_view.route('/board', methods=['GET', 'POST'])
# @login_required
# def board():
#     return render_template('layout-board.html')

# #게시판 글
# @guide_view.route('/board/view', methods=['GET', 'POST'])
# @login_required
# def board_view():
#     return render_template('layout-board-view.html')

# #댓글 추가
# @guide_view.route('/comment/add', methods=['GET', 'POST'])
# @login_required
# def comment_add():
#     return render_template('/board/view')

# #댓글 수정
# @guide_view.route('/comment/update/<int:id>', methods=['GET', 'POST'])
# @login_required
# def comment_update():
#     return render_template('/board/view')

# #댓글 삭제
# @guide_view.route('/comment/delete/<int:id>')
# @login_required
# def comment_delete():
#     return render_template('/board/view')

# #답글 추가
# @guide_view.route('/reply/add', methods=['GET', 'POST'])
# @login_required
# def comment_add():
#     return render_template('/board/view')

# #답글 수정
# @guide_view.route('/reply/update/<int:id>', methods=['GET', 'POST'])
# @login_required
# def reply_update():
#     return render_template('/board/view')

# #답글 삭제
# @guide_view.route('/reply/delete/<int:id>')
# @login_required
# def reply_delete():
#     return render_template('/board/view')