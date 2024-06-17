#Attention, this code only works if you are in Replit because it includes a Replit function.

from replit import db
import datetime, os, time

db["password"] = "Hello123"

password = input("Enter password: ")
timestamp = datetime.datetime.now()

def add():
  add1 = input("Here is your diary:\n>  ")
  db[timestamp] = add1

def view():
  keys = db.keys()
  for key in keys:
    if key == "password":
      continue
    print(f"{key} {db[key]}")
    time.sleep(0.2)

while True:
  time.sleep(2)
  os.system("clear")
  if password != db["password"]:
    print("Wrong password")
    break
  else:
    input1 = input("1: Add\n2: View\n> ")
    if input1 == "1":
      add()
      time.sleep(0.4)
      os.system("clear")
    elif input1 == "2":
      view()
      time.sleep(1)
      os.system("clear")