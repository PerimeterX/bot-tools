# Lab Five - Detect Good Bots

## Description
Not all bots are bad. Many bots are used to automate tasks that are actually beneficial for your site. For example - search crawlers, that scan your site and help drive search traffic to it.

In this lab we will enhance the application to detect and whitelist Googlebot, and block malicious users pretending to be Googlebot.

Good bots typically follow 4 rules:

1. *Declare who you are* - using the user-agent to announce who you are, and typically provide in it a URL to find more about the bot.
2. *Follow rules to validate your identity* - provide a mechanism to find out if the request using the user-agent is actually the good bot, and not a pretender. a common way is to restrict the bots to come from a set of IP addresses registered to the service running the bot.
3. *Respect robots.txt rules*
4. *Behave nicely* - specifically, don't be too aggressive when you crawl, and offer ways to limit and control the bots behavior on the site.

## Requirements

## Instructions
Implement the rules to detect and whitelist Googlebot:
* Googlebot will always identify itself with the stringe `Googlebot` in the user-agent. See https://support.google.com/webmasters/answer/1061943
* Googlebot follows the reverse-dns rule:
  * perform a reverse dns on the IP address from which a googlebot request is received
  * verify that the hostname received is in one of the domains: `google.com` or `googlebot.com`
  * resolve the hostname you received, and verify that the IP address you receive is the same as the IP address you started with
  * see https://support.google.com/webmasters/answer/80553?hl=en
  * Example for a googlebot IP is 66.249.73.49. To test that the detection is working set the XFF header as follows: `X-Forwarded-For: 66.249.73.49` 

## Notes
* Many other crawlers follow the same logic that was set by Google.
* Pretending to be a goodbot by using their user-agent is a common trick used by bad bots hoping to get in. Surprisingly many sites are still whitelisting known crawler user-agents without any additional validation on the IP address from which the request arrived.

## Application Code Snippet
```
# Lab 5
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

```
