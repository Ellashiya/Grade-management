from flask import Flask, render_template
import sys
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/planner/month')
def planner_month():
    return render_template('layout-planner-month.html')

if __name__ == '__main__':
    app.run(debug=True)