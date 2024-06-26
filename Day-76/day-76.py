from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Banana man!'


@app.route('/portfolio')
def portfolio():
    page = """<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
</head>

<body>
<h1> My Portfolio</h1>
<h2>Day-66 Solution</h2>
<p>So, day 66 was all about UI and how to use TKinter.<br>I find the projekt wery cool becouse we made a calculater app.<br>I find it so cool because i can use it dayly. i even have the code on my Iphone.


<img src="static/images/code.png"width="500" height="410">
<img src="static/images/calculater.png"width="300" height="410">
<a href="https://replit.com/~">Replit Home</a>
</body>

</html>"""
    return page


@app.route('/linktree')
def linktree():
    page = """<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
</head>

<body>
<img src="static/images/me.png" height="50%" width="40%">

<h1>Banana Man</h1>
<h2>the most banana man in the world</h2>
<h1 style="margin-top: 10%;">Socials</h1>

<a href="https://www.twitch.tv/quickcodebro">Twitch account </a>

</body>

</html>"""
    return page


app.run(host='0.0.0.0', port=81)
