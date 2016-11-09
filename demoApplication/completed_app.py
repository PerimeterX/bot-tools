# Import the Flask Framework
from flask import Flask, render_template, request, Response, redirect, escape
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Import the fixer
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


@app.route('/')
def index():
    """Return the index page"""
    if 'fpid' in request.cookies:
        return "Welcome :-)"
    else:
        return app.send_static_file('html/index.html')


@app.route('/badbots')
def badbots():
    """Return the badbots page"""
    if checkBadUseragent():
        return "Sorry bad bot, but you are not permitted.", 403
    else:
        return "Welcome to lab 1!"


@app.route('/cloudvendor')
def cloudvendor():
    """Return the cloud vendor page"""
    reader = maxminddb.open_database('cloud.mmdb')
    isCloud = reader.get(request.remote_addr)
    if isCloud:
        return "Sorry but cloud vendors are not permitted.", 403
    else:
        return "Looks like you visited from a good IP."


@app.route('/useragent')
def useragent():
    """Return the useragent page"""
    return render_template('navigator.html',
                           userAgent=request.headers.get('user-agent'))


@app.route('/phantomjs')
def phantomjs():
    """Return the phantomjs page"""
    return render_template('phantomjs.html',
                           userAgent=request.headers.get('user-agent'))


@app.route('/googlebot')
def googlebot():
    """Return the googlebot page"""
    googlebot = re.compile('Googlebot')
    m = googlebot.search(request.headers.get('user-agent'))
    if m:
        isGooglebot = verifyGooglebotAddr()
    else:
        isGooglebot = "Not a Googlebot user-agent"
    return render_template('googlebot.html', isGooglebot=str(isGooglebot))


def verifyGooglebotAddr():
    """Function to verify if a bot comes from Google"""
    p = re.compile('^.+\.(googlebot|google)\.com$')
    try:
        reversed_dns = socket.gethostbyaddr(request.remote_addr)
    except:
        m = False
    else:
        m = p.match(reversed_dns[0])
    if (m and request.remote_addr == socket.gethostbyname(reversed_dns[0])):
        return "Validated Googlebot"
    else:
        return "Fake Googlebot - invalid IP address"


@app.route('/content')
def content():
    return render_template('content.html')


@app.route('/content/<path:path>')
@limiter.limit("15/minute", error_message='Slow down cowboy!')
def content_pages(path):
    return render_template('content_page.html', pageInfo=str(path))


@app.route('/hidden')
def hidden():
    bannedIpList.append(request.remote_addr)
    return "You should not be visiting this page. Please respect the robots.txt file.", 403

#create robots.txt file
@app.route('/robots.txt')
def robotstxt():
    return Response("User-agent: *\nDisallow: /hidden", mimetype="text/plain")

@app.before_request
def checkBannedIPs():
    if request.remote_addr in bannedIpList:
        return "You are not allowed to visit this page", 403


def checkBadUseragent():
    """Function to verify if the user-agent is of some declared bad bot"""
    # Cited from 
    # 6G FIREWALL/BLACKLIST
    # @ https://perishablepress.com/6g/
    badbot = re.compile(
        'binlar|casper|checkpriv|choppy|clshttp|cmsworld|diavol|dotbot|extract|feedfinder|flicky|g00g1e|harvest|heritrix|httrack|kmccrew|loader|miner|nikto|nutch|planetwork|postrank|purebot|pycurl|python|seekerspider|siclab|skygrid|sqlmap|sucker|turnit|vikspider|winhttp|xxxyy|youda|zmeu|zune',
        re.IGNORECASE)
    isBadBot = badbot.search(request.headers.get('user-agent'))
    print isBadBot
    if isBadBot != None:
        return True
    else:
        return False


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
