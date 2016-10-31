# Lab Two - IP Blacklisting

## Description
In many cases you can tell that a client is bad based on the IP source it is
coming from. For example - if we can detect that a client arrives from a cloud or
hosting vendor, it is likely that this isn't a human.
There are different resources to get lists of IP addresses used for IP classification.

Some common suspicious resources are:

* IP ranges of cloud and hosting vendors
* IP addresses used by known proxies and anonymizing services
* IP addresses that were flagged as bad reputation due to detecting attacks or
other malicious activity from them.

In this lab you learn to build your own IP database using the MaxMind DB format.

## Requirements
* a databse file including AWS IP ranges and Google Cloud IP ranges in maxminddb format (provided in this folder)
* Google Chrome with the ModHeader extension

## Instructions
Use the example database file to enhance the site to block requests coming from
cloud vendors.
To simulate cloud IP addresses you can use the ModHeader to "fake" your IP addresses
using the `X-Forwarded-For` header.

Example:`X-Forwarded-For: 54.240.236.40`

Visit http://localhost:5000/cloudvendor and verify you are now blocked.



## Application Code Snippet

```
# Lab 2
@app.route('/cloudvendor')
def cloudvendor():
    """Return the cloud vendor page"""
    reader = maxminddb.open_database('cloud.mmdb')
    isCloud = reader.get(request.remote_addr)
    if isCloud:
        return "Sorry but cloud vendors are not permitted.", 403
    else:
        return "Looks like you visited from a good IP."
```
