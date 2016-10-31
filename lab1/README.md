# Lab One - Checking User-Agent for Bad Bots

## Description
This lab goes over the basics of checking for known bad user-agents. These are bots that announce their identities. 

## Requirements
* web browser
* browser extention to change the user-agent string

## Instructions
Instructions will use Google [Chrome](https://www.google.com/chrome/) and the extension [ModHeader](https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj)

Click the ModHeader extension and add a new user-agent. 

  Example UA: ***Nikto Web Scanner***
  
Visit [http://localhost:5000/badbots](http://localhost:5000/badbots) and verify you are now blocked.

## Notes
The following is an expression to match a list of known bots:
'(archive\.org|binlar|casper|checkpriv|choppy|clshttp|cmsworld|diavol|dotbot|extract|feedfinder|flicky|g00g1e|harvest|heritrix|httrack|kmccrew|loader|miner|nikto|nutch|planetwork|postrank|purebot|pycurl|python|seekerspider|siclab|skygrid|sqlmap|sucker|turnit|vikspider|winhttp|xxxyy|youda|zmeu|zune)'

taken from: https://perishablepress.com/6g/
other resources for lists of known bots:
https://github.com/JayBizzle/Crawler-Detect/blob/master/src/Fixtures/Crawlers.php

## Application Code Snippet
```
# Lab 1
@app.route('/badbots')
def badbots():
    """Return the badbots page"""
    if checkBadUseragent():
        return "Sorry bad bot, but you are not permitted.", 403
    else:
        return "Welcome to lab 1!"

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
```
