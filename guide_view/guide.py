from flask import Flask, Blueprint, request, render_template

guide_app = Blueprint('guide', __name__)

@guide_app.route('/test')
def test():
    return render_template('index.html') # test

@guide_app.route('/')
def main():
    return render_template("index.html")

@guide_app.route('/register')
def register():
    return render_template('register.html')

@guide_app.route('/login')
def login():
    return render_template('login.html')

@guide_app.route('/password')
def password():
    return render_template('password.html')

@guide_app.route('/planner/month')
def planner_month():
    return render_template('layout-planner-month.html')

@guide_app.route('/planner/day')
def planner_day():
    return render_template('layout-planner-day.html')

@guide_app.route('/schoolgrades')
def schoolgrades():
    return render_template('layout-schoolgrades.html')

@guide_app.route('/mockexam')
def mockexam():
    return render_template('layout-mockexam.html')

@guide_app.route('/mock/board')
def mock_board():
    return render_template('layout-mock-board.html')

@guide_app.route('/general/board')
def general_board():
    return render_template('layout-general-board.html')

@guide_app.route('/401')
def error_401():
    return render_template('401.html')

@guide_app.route('/404')
def error_404():
    return render_template('404.html')

@guide_app.route('/500')
def error_500():
    return render_template('500.html')