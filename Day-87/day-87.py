import os
from flask import Flask, redirect, request, session
from replit import db

app = Flask(__name__)
app.secret_key = os.urandom(24)

db["user"] = {"username": "code", "password": "banana"}


@app.route("/register", methods=["POST"])
def register():
  keys = db.keys()
  form = request.form
  if form["username"] not in keys:
    db[form["username"]] = {"name": form["name"], "password": form["password"]}
    return redirect("/login")
  else:
    return "Username already exists"


@app.route("/blog", methods=["POST", "GET"])
def blog():
  if request.method == "POST":
    title = request.form["title"]
    date = request.form["date"]
    text = request.form["text"]
    f = open("print.html", "r")
    page = f.read()
    f.close()
    message = {"title": title, "date": date, "text": text}
    db["blog_messages"] = db.get("blog_messages", []) + [message]

  with open("blog.html", "r") as f:
    page = f.read()

  messages = db.get("blog_messages", [])
  for message in messages:
    page += f"<h2>{message['title']}</h2><p>{message['date']}</p><p>{message['text']}</p><hr>"

  return page


@app.route('/')
def index():
  username = request.headers["X-Replit-User-Name"]
  return redirect('/blog')


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
