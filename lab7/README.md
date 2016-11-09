# Lab Seven - Checking the Navigator User-Agent

## Description
This lab shows how to identify a mismatch in the user-agent sent by a browser in the HTTP headers and compare it to the navigator.userAgent property of the DOM.

For more information and additional properties of the Navigator object visit https://developer.mozilla.org/en-US/docs/Web/API/Navigator

## Requirements

* web browser
* browser extention to change the user-agent string

## Instructions
Instructions will use Google [Chrome](https://www.google.com/chrome/) and the extension [ModHeader](https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj)

1. Visit [http://localhost:5000/useragent](http://localhost:5000/useragent) and observe the user-agent sent by the browser and the Navigator obect user-agent are the same.
2. Click the ModHeader extension and add a new user-agent. 

  Example User-Agent: ***Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)***

3. Refresh the URL. What do you observe? There is now a mismatch between the user-agent sent in the HTTP header and what is reported from the navigator object.

## Notes
User-agent is one of many signals to be used to detect a bot that spoofs it's identity. Alone it is not enough, but when combined with other signals it can be very useful.

## Application Code Snippet
```
# Lab 7
@app.route('/useragent')
def useragent():
    """Return the useragent page"""
    return render_template('navigator.html',
                           userAgent=request.headers.get('user-agent'))
```
