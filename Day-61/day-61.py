#Attention, this code only works if you are in Replit because it includes a Replit function.

from replit import db
import datetime, os

while True:
  choice = input("""Do you want to:
1. Add a tweet
2.View tweets\n""")
  os.system("clear")
  if choice == "1":
    tweet = input("What would you like to tweet?\n")

    time = datetime.datetime.now()
    db[time] = tweet
    os.system("clear")
  elif choice == "2":
    keys = db.keys()
    count = 0

    for key in keys:
      print(key, db[key])
      print("\n")
      count += 1
      if count % 10 == 0:
        carryon = input("Do you want to see another 10 tweets?\n")
        os.system("clear")

        if carryon == "no":
          break
        elif carryon == "yes":
          continue