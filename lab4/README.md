# Lab Four - Catching Scrapers with Hidden Links

## Description
In this lab we will take on the offense, and plant traps for scrapers and crawlers that will help us detect and block them.
To trick the scrapers we will set a hidden link, that will actually not render on a real browser.

Typically crawlers are not actually rendering the pages, but instead are parsing the html page and looking for links, and will use the found links to populate the list of pages to crawl.
To instruct legitimate crawlers to not click this link it is advised to add the `rel="nofollow"` to the link.

Setting such special links will help flag bad crawlers, no human will request the page in a natural way.

## Requirements
* scrapy bot or wget
* wget docker image: `docker pull mwendler/wget`

## Instructions
We have seen in the previous lab that scrapy when tuned properly at a moderate rate can scrape the entire site.
* Update the application to include in every page a hidden link with instruction to not click it that directs to the path "/hidden" like this: `<a rel="nofollow" style="display:none;" href="/hidden">hidden link</a>`
* Create a rule, that blocks anyone accessing the hidden "forbidden" page.
* as accessing such a page is a clear indication of a malicious user, so we would like to mark the IP address of the user and add it to a block list.

Example: `wget -e robots=off --header="X-Forwarded-For: 1.2.3.4"  -r http://localhost:5000/content`

## Notes
For the simplicity of this exercise we will be using an IP address for the blocking. However, be advised that blocking by IP address only may also block legitimate users sharing the IP address (for instance in a coffee house or office).

## Application Code Snippet

```
# Lab 4
@app.route('/content')
def content():
    return render_template('content.html')


@app.route('/content/<path:path>')
def content_pages(path):
    return render_template('content_page.html', pageInfo=str(path))


@app.route('/hidden')
def hidden():
    bannedIpList.append(request.remote_addr)
    return "You should not be visiting this page. Please respect the robots.txt file.", 403


@app.before_request
def checkBannedIPs():
    if request.remote_addr in bannedIpList:
        return "You are not allowed to visit this page", 403
```
