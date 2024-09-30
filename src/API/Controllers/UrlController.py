
from src.API import app

from flask import Flask, jsonify, redirect, render_template, request, url_for
from src.core.Domain.Services.UrlService import *
from src.core.Domain.Services.UrlService import UrlService
from src.core.Domain.models.URL import URL

@app.route('/url/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        original_url = request.form['original_url']
        new_url = URL(original_url=original_url, short_url="")
        url_object=Save_Url(new_url)
        return jsonify(url_object.to_json_shotUrl())
    
    return render_template('index.html')

@app.route('/url/<short_url>')
def redirect_to_url(short_url):
    url = find_by_short_url_(short_url=short_url)
    if url is None:
        # URL not found
        return 'URL Not found ', 404
    return redirect(url.original_url)