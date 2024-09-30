
from flask import render_template
from src.API import app
from src.API.Controllers import UrlController

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')
