# Bot-Tools

This repository will host all the resources used and shared for the [tutorial session](http://conferences.oreilly.com/security/network-data-security-ny/public/schedule/detail/52989) in O'Reilly Security NY.

At this point this repository contains only the instructions and requirements on what should participants download and preinstall prior to the session.
The specific scripts and tools user in the session, such as specific tools and web-bots, and a sample test site to experiment with will be provided here before the session starts.

## Required packages and tools
Please install the following packages and tools prior to the session:

* Install Docker. You can download and find instructions on how to install docker for your OS here: https://www.docker.com/products/overview
  * Docker for Windows requirements are 64bit Windows 10 Pro, and the Hyper-V package enabled. 
  * If you have a different windows version - see https://docs.docker.com/engine/installation/windows/ on how to install docker with Docker Toolbox.
  * In case you can't install docker, you will need to install node.js for your OS. You can download node.js here https://nodejs.org/en/download/
* Install python 2.7.
  * Windows: download the latest python version at: https://www.python.org/downloads/
  * Mac:
    * Check if you already have python installed and its version by running `python -V` on the command line
    * If you have brew - run `brew install python`
    * or go to https://www.python.org/downloads/ to download python for MacOSX
* Install Chrome
* Install ModHeader Chrome extension - https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj

## Docker images
Verify that Docker is running, and from the command line install the following images:

* Scrapy
```bash
docker pull aciobanu/scrapy
```
* CasperJS
```bash
docker pull zopanix/casperjs
```
* Selenium
```bash
docker pull selenium/hub
docker pull selenium/node-chrome
```

## Node packages (if you didn't install docker)
* Install PhantomJS: http://phantomjs.org/download.html
* Install CasperJS:
```bash
npm install casperjs
node_modules/casperjs/bin/casperjs selftest
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

## [Lab 1](https://github.com/PerimeterX/bot-tools/tree/master/lab1) - Checking User Agent for Bad Bots

## [Lab 2](https://github.com/PerimeterX/bot-tools/tree/master/lab2) - Blocking Users from Cloud Hosting and Malicious IP Addresses

## [Lab 3](https://github.com/PerimeterX/bot-tools/tree/master/lab3) - Rate Limiting

## [Lab 4](https://github.com/PerimeterX/bot-tools/tree/master/lab4) - Catching Scrapers with Hidden Links

## [Lab 5](https://github.com/PerimeterX/bot-tools/tree/master/lab5) - Identifying Good Crawlers

## [Lab 6](https://github.com/PerimeterX/bot-tools/tree/master/lab6) - Challenging with Javascript

## [Lab 7](https://github.com/PerimeterX/bot-tools/tree/master/lab7) - Checking User Agent Take 2 (Navigator)

## [Lab 8](https://github.com/PerimeterX/bot-tools/tree/master/lab8) - Finding Traces of PhantomJS
