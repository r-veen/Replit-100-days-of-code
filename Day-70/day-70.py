import os

normal = os.environ['normal']
admin = os.environ['admin']

userPass = input("Password \n> ")

if userPass == normal or admin:
  if userPass == normal:
    print("Hello normal user")
  else:
    print("Welcome admin")
else:
  print("Better luck next time")
