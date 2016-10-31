// https://gist.github.com/gaspanik/5609135 original credit 
//
var screenshotUrl = 'http://example.com/'

var casper = require("casper").create({
	verbose: true,
	logLevel: 'debug',
	viewportSize: {
        width: 1024,
        height: 768
    }
});

if (casper.cli.args.length < 1) {
  casper
    .echo("Usage: $ casperjs capture.js http://example.com")
    .exit(1)
  ;
} else {
  screenshotUrl = casper.cli.args[0];
  screenshotName = casper.cli.args[1];
}

casper.start(screenshotUrl, function() {
	this.wait(3000);
    this.capture(screenshotName, {
        top: 0,
        left: 0,
        width: 1024,
        height: 768
    });
});

casper.run();
