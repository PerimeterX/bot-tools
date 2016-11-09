# Bot-Tools

This repository will host all the resources used and shared for the tutorial session in [O'Reilly Security NY](http://conferences.oreilly.com/security/network-data-security-ny/public/schedule/detail/52989) and [O'Reilly Security EU](http://conferences.oreilly.com/security/network-data-security-eu/public/schedule/detail/53016).

At this point this repository contains only the instructions and requirements on what should participants download and preinstall prior to the session.
The specific tools, test site and instructions are provided in the session itself, and will be updated and published once the tutorial session is done.

## Please install the following prior to the session:
### Required packages and tools
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

### Docker images
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

### Node packages (if you didn't install docker)
* Install PhantomJS: http://phantomjs.org/download.html
* Install CasperJS:
```bash
npm install casperjs
node_modules/casperjs/bin/casperjs selftest
```

# The following will be done and used during the session itself:
## Usage

Clone this repository to your selected folder
```
git clone https://github.com/PerimeterX/bot-tools.git
```

## Build Docker
From the repository directory do the following:
```bash
cd demoApplication
docker build -t bot-lab-demo:latest .
```
to run application natively on your machine using python see instructions below

## Run Docker
`docker run -ti -p 5000:5000 bot-lab-demo`

## Run application locally
instead of running it in a docker container, the application can run locally using python. To do that do the following:
```bash
cd demoApplication
pip install -r requirements.txt
python app.py
```

## Docker commands
In case you aren't familiar with docker - here are a few commands that can help you get started, and should be sufficient for this tutorial:

Download an image, and all its parents, from the registry: 
```
docker pull <image name>
```
Start and stop a container: 
```docker start/stop <container name>
```
To check the running containers execute: 
```docker ps
```
To show last 50 lines and follow the log output of the container execute: 
```docker logs --tail=50 -f <container name>
```
To check the running and stopped containers execute: 
```docker ps -a
```
To show the list of the images run: 
```docker images
```
To run a command inside the container namespace you run the following docker command: 
```docker exec -ti <container name> <command>
```
This is very useful when you want to connect to a running container and work inside of the container. 
```docker exec -ti <container name> bash
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
