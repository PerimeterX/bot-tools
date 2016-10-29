# bot-tools

This repository contains the resources to help you build a test-lab to run different web-bots and a sample test-site to run them against it.

## Pre-requisites
* Install Docker. You can download and find instractions on how to install docker for your OS here: https://www.docker.com/products/overview
* Install python 2.6 or later.
  * Windows: download the latest python version at: https://www.python.org/downloads/
  * Mac: 
    * use Mac's python
    * use brew to install python (brew install python)

## Install packages
* Verify that Docker is running
* Install PhantomJS docker
```bash
$ docker pull wernight/phantomjs
```
* Install Selenium docker:
```bash
$ docker pull selenium/hub
$ docker pull selenium/node-chrome
```
