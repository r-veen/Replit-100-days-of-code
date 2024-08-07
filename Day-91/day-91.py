import requests, json, os, time
from replit import db

while True:
  time.sleep(1)
  os.system("clear")
  result = requests.get("https://icanhazdadjoke.com/",
                        headers={"Accept": "application/json"})
  joke = result.json()

  jk = joke["joke"]
  id = joke["id"]
  print(jk)
  obtion = input("(s)ave joke, (l)oad old jokes, (n)ew joke\n>  ")
  print(joke["joke"])
  if obtion == "s":
    db[id] = jk
    print("\nSAVED\n")
    continue
  if obtion == "l":
    keys = db.keys()
    for key in keys:
      result = requests.get(f"https://icanhazdadjoke.com/j/{key}",
                            headers={"Accept": "application/json"})
      joke = result.json()
      print(joke["joke"])
      print("\n")
      time.sleep(4.5)

  if obtion == "n":
    continue
