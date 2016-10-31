# Bot-Tools

This repository will host all the resources used and shared for the [tutorial session](http://conferences.oreilly.com/security/network-data-security-ny/public/schedule/detail/52989) in O'Reilly Security NY.

At this point this repository contains only the instructions and requirements on what should participants download and preinstall prior to the session.
The specific scripts and tools user in the session, such as specific tools and web-bots, and a smaple test site to experiment with will be provided here before the session starts.

## Required packages and tools
Please install the following packages and tools prior to the session:
* Install Docker. You can download and find instractions on how to install docker for your OS here: https://www.docker.com/products/overview
* Install python 2.7.
  * Windows: download the latest python version at: https://www.python.org/downloads/
  * Mac:
    * Check if you already have python installed and its version by running `python -V` on the command line
    * If you have brew - run `brew install python`
    * or go to https://www.python.org/downloads/ to download python for MacOSX
* Install Chrome
* Install ModHeader Chrome extension - https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj

## Docker images
* Verify that Docker is running, and from the command line install the following images:
* Scrapy
```bash
$ docker pull aciobanu/scrapy
```
* CasperJS
```bash
$ docker pull zopanix/casperjs
```
* Selenium
```bash
$ docker pull selenium/hub
$ docker pull selenium/node-chrome
```

# Usage

## Build Docker
```
$ cd demoApplication
$ docker build -t bot-lab-demo:latest .
```
to run application natively on your machine using python see instructions below

## Run Docker
`docker run -ti -p 5000:5000 bot-lab-demo`

## Run application locally
instead of running it in a docker container, the application can run locally using python. To do that do the following:
```
$ cd demoApplication
$ pip install -r requirements.txt
$ python app.py
```

## Notes
Each lab folder contains a README.md containing a short description, instructions, and any supporting files required.

## Lab 1 - Checking User Agent for Bad Bots

## Lab 2 - Blocking Users from Cloud Hosting and Malicious IP Addresses

## Lab 3 - Rate Limiting

## Lab 4 - Catching Scrapers with Hidden Links

## Lab 5 - Identifying Good Crawlers

## Lab 6 - Challenging with Javascript

## Lab 7 - Checking User Agent Take 2 (Navigator)

## Lab 8 - Finding Traces of PhantomJS
