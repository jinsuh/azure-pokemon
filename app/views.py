from flask import render_template, send_from_directory
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('material.html')

# @app.route('/js/<path:path>')
# def send_js(path):
#     return send_from_directory('js', path)