from flask import flask, render_template
from project_a.py import * 

@app.route('/')
def init():
    init_template = "Welcome.html"
    return render_template(init_template)

@app.route('/results')
def results():
    return None

if __name__ == "main":
    app.run()
    