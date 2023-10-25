from flask import Flask, render_template
import sys
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/password')
def password():
    return render_template('password.html')

@app.route('/planner/month')
def planner_month():
    return render_template('layout-planner-month.html')

@app.route('/planner/day')
def planner_day():
    return render_template('layout-planner-day.html')

@app.route('/schoolgrades')
def schoolgrades():
    return render_template('layout-schoolgrades.html')

@app.route('/mockexam')
def mockexam():
    return render_template('layout-mockexam.html')

@app.route('/mock/board')
def mock_board():
    return render_template('layout-mock-board.html')

@app.route('/general/board')
def general_board():
    return render_template('layout-general-board.html')

@app.route('/401')
def error_401():
    return render_template('401.html')

@app.route('/404')
def error_404():
    return render_template('404.html')

@app.route('/500')
def error_500():
    return render_template('500.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)