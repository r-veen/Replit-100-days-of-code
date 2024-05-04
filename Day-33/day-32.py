import time, os

print("To Do List Manager: ")
time.sleep(1)
list = []
times = 0
def printlist():
  print(*list, sep='\n')
while True:
  times += 1
  answer = input("Do you want to view, add, or edit your to do list?\n ")
  time.sleep(1)
  os.system("clear")
  if answer == "view":
    printlist()
  elif answer == "add":
    add = input("What do you wahnt to add?\n ")
    list.append(add)
  elif answer == "edit":
    remove = input("What do you have. What can i remove\n ")
    if remove in list:
      list.remove(remove)
    else:
      print("That is not in the list")
  else:
    print("I dont have this option")
  if times > 5:
    exit = input("Exit?\n")
    if exit == "yes":
      break