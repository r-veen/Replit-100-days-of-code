from flask import Flask

app = Flask(__name__)

myReflections = {}

myReflections["75"] = {"link" : "https://replit.com/@replit/Day-75-Solution", "Reflection" : "i did not find it hard."}

myReflections["76"] = {"link" : "https://replit.com/@replit/Day-76-Solution", "Reflection" : "not that hard."}


@app.route('/<pageNumber>')
def index(pageNumber):
  global myReflections
  page = ""
  f = open("Day-78/template/day-78.html", "r")
  page = f.read()
  f.close()

  
  page = page.replace("{day}", pageNumber)
  page = page.replace("{link}", myReflections[pageNumber]["link"])
  page = page.replace("{reflection}", myReflections[pageNumber]["Reflection"])
  
  
  return page


app.run(host='0.0.0.0', port=81)