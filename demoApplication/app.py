# Import the Flask Framework
from flask import Flask, render_template, request, Response, redirect, escape
app = Flask(__name__)

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Import the  Proxy fixer
from werkzeug.contrib.fixers import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)

#Rate Limit Configuration

limiter = Limiter(app, key_func=get_remote_address)

# Import non-Flask libs
import requests
import json
import socket
import re
import maxminddb

# Banned list
bannedIpList = []

# Lab 6
@app.route('/')
def index():
    """Return the index page"""
    return "Welcome to bot test lab"

# Lab 1
@app.route('/badbots')
def badbots():
    """Return the badbots page"""
    return "Welcome to lab 1!"

# Lab 2
@app.route('/cloudvendor')
def cloudvendor():
    """Return the cloud vendor page"""
    return "Welcome to lab 2!"


# Lab 7
@app.route('/useragent')
def useragent():
    """Return the useragent page"""
    return "Welcome to lab 7!"

# Lab 8
@app.route('/phantomjs')
def phantomjs():
    """Return the phantomjs page"""
    return "Welcome to lab 8!"

# Lab 5
@app.route('/googlebot')
def googlebot():
    """Return the googlebot page"""
    return "Welcome to lab 5!"

# Lab 3 & 4
@app.route('/content')
def content():
    return render_template('content.html')

@app.route('/content/<path:path>')
def content_pages(path):
    return render_template('content_page.html', pageInfo=str(path))

@app.route('/hidden')
def hidden():
    return "Hidden page - you shouldn't be here!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
