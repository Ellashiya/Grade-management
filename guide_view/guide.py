from flask import Flask, Blueprint, request, render_template

guide_view = Blueprint('guide_view', __name__, static_folder="static", template_folder="templates")

@guide_view.route('/')
def main():
    return render_template("index.html")

@guide_view.route('/register')
def register():
    return render_template('register.html')

@guide_view.route('/login')
def login():
    return render_template('login.html')

@guide_view.route('/password')
def password():
    return render_template('password.html')

@guide_view.route('/planner')
def planner():
    return render_template('layout-planner.html')

@guide_view.route('/grades')
def grades():
    return render_template('layout-grades.html')

@guide_view.route('/board')
def board():
    return render_template('layout-board.html')