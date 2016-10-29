# bot-tools

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

## Docker images
* Verify that Docker is running
* CasperJS 
```bash
$ docker pull zopanix/casperjs
```
* Selenium
```bash
$ docker pull selenium/hub
$ docker pull selenium/node-chrome
```
