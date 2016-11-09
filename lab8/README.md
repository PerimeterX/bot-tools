# Lab Eight - Checking for PhantomJS

## Description
This lab shows an introduction to identifying PhantomJS by looking for the specific DOM objects named window.phantom and window.callPhantom.

## Requirements
* Computer with PhantomJS installed or Docker image

## Instructions
This lab will use the Docker image `zopanix/casperjs`. To install run `docker pull zopanix/casperjs`. 

Open the URL [http://localhost:5000/phantomjs](http://localhost:5000/phantomjs) with your web browser. 

Now run the following command to execute the PhantomJS script. 

Mac or Linux:
```
docker run --rm  -v $PWD:/data --net="host" zopanix/casperjs default_phantom.js http://<machine-ip>:5000/phantomjs results_default_phantom.png
```
Windows:
```
docker run --rm  -v %cd%:/data --net="host" zopanix/casperjs default_phantom.js http://<machine-ip>:5000/phantomjs results_default_phantom.png
```

The results are saved to `results_default_phantom.png`. 
This is a screenshot of the browser view. See the default PhantomJS user-agent.

Now run the updated script that changes the user-agent (note that this command will also change `navigator.userAgent`).

Mac or Linux:
```
docker run --rm  -v $PWD:/data --net="host" zopanix/casperjs spoofedUA_phantom.js  http://<machine-ip>:5000/phantomjs results_phantom.png
```
Windows:
```
docker run --rm  -v %cd%:/data --net="host" zopanix/casperjs spoofedUA_phantom.js  http://<machine-ip>:5000/phantomjs results_spoofed_phantom.png
```

Open the file `results_spoofed_phantom.png` and you can see how PhantomJS changes both the user-agent string send in the headers and the Navigator object. Still, the window.phantom object exists and can be used to identify PhantomJS visitors.

## Application Code Snippet
```
# Lab 8
@app.route('/phantomjs')
def phantomjs():
    """Return the phantomjs page"""
    return render_template('phantomjs.html',
                           userAgent=request.headers.get('user-agent'))

```
