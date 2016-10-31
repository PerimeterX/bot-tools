# Lab Three - Rate Limiting

## Description
Bots can be aggressive at times, when crawling your site, or trying to brute force
some task (such as a login form). Coming at such a high rate also taxes your infrastructure.
A simple way to manage that is to add rate limiting rules, which will prevent a user from performing too many requests in a given time. This will typically not impact legitimate users, as they perform tasks in a moderate (human) pace.

## Requirements
* Scrapy bot or wget
* wget docker image: `docker pull mwendler/wget`
* to simplify wget commands use `alias wget='docker run --rm mwendler/wget'` (Mac or Linux)

## Instructions
Add rate-limiting rules to the application, to limit IP addresses to perform no more than 15 requests per minute.
Configure scrapy to scrape the site:
* initially at maximum speed, and see that it is blocked
* tune the rate in which scrapy requests pages, to bypass the threshold limitation, and scrape the entire site.

Refresh the page many times (15).

## Notes

## Application Code Snippet

```
@app.route('/content')
@limiter.limit("15/minute", error_message='Slow down cowboy!')
def content():
    return render_template('content.html')
```
