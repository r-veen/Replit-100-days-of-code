from flask import Flask, request

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
  if request.form["wood"] == "no" and request.form["color"] == "orange".lower(
  ) and request.form["food"] == "banana":
    return "You're not a robot!"
  else:
    return "You're a robot!"


@app.route('/')
def index():
  page = """<form method="post" action="/login">
  <p>Are you made of wood?: 
    <input type="radio" name="wood" value="yes" required> Yes
    <input type="radio" name="wood" value="no" required> No
  </p>
  <p>Wich color is orange?: <input type="text" name="color" required></p>
  <p>Wich of these foods is your favorit?: 
    <select name="food" required>
      <option value="wood">wood</option>
      <option value="banana">Banana</option>
      <option value="metal">metal</option>
    </select>
  </p>
  <button type="submit">Finished</button>

</form>"""
  return page


app.run(host='0.0.0.0', port=81)
