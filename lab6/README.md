# Lab Six - Performing a Javascript Challenge

## Description
This lab shows how to perform a basic Javascript challenge to prevent primitive (non-Javascript) based bots from accessing the site.

## Requirements
* web broswer
* extension to disable Javascript - [Toggle JS](https://chrome.google.com/webstore/detail/toggle-javascript/cidlcjdalomndpeagkjpnefhljffbnlo)
* extension to view cookies - [Edit This Cookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg)
* command line tool - [cURL](https://curl.haxx.se/)

## Instructions

Install the require browser extensions before starting.

Visit [http://localhost:5000](http://localhost:5000) with your browser. Notice that you receive the welcome page without any issues.

Now use Edit This Cookie to delete your cookies and then use Toggle JS to disable Javascript. The page will now refresh. What message do you see?

What is happening? At the application (or web server) we look for the presense of our verification cookie. If the cookie is not present with the request the server response with a default challenge page. This page contains a small piece of Javascript which sets a the cookie. In our example we create a very simple cookie only, but a production implementation will use the server to set a more secure cookie that cannot be easily forged by signing it with an HMAC and keeping it time based. The token can be refreshed using Javascript in the background, enhancing the user-experience.

## Application Code Snippet

```
# Lab 6
@app.route('/')
def index():
    """Return the index page"""
    if 'fpid' in request.cookies:
        return "Welcome :-)"
    else:
        return app.send_static_file('html/index.html')
```
