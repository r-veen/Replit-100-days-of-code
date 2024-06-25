from replit import db
import random, os, time

#This only works in replit

while True:
  inp = input("1: New User\n2: Login\n3: Quit\n> ")
  if inp == "1":
    username = input("Username: ")
    password = input("Password: ")
    salt = random.randint(1000, 9999)
    password = hash(password)
    db[username] = {"password": password, "salt": salt}
    print("Account Created")
    time.sleep(2)
    os.system("clear")
  if inp == "2":
    username = input("Username: ")
    password = input("Password: ")
    salt = db[username]["salt"]
    password = hash(password)
    if db[username]["password"] == password:
      print("Login Successful")
      time.sleep(3)
      os.system("clear")
    else:
      print("Login Failed")
      time.sleep(3)
      os.system("clear")
  elif inp == "3":
    break
