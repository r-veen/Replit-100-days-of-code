import os, time, random

debugmode = False
fileExist = None

print("To Do List Manager: ")
print()

myEvent = []

files = os.listdir()
if "quickSave.txt" in files:
  fileExist = True
if "quickSave.txt" not in files:
  print("Error: Quick Save not found.")

try:
  f = open("Todo.txt", "r")
  myEvent = eval(f.read())
  f.close()
except Exception as err:
  print("Error: unable to load.")
  if debugmode:
    print(err)


def view():
  print()
  for idx, row in enumerate(myEvent):
    print(f"{idx}: {row[0]}")
  print()


def edit():
  try:
    edit1 = int(input("Which number? "))
    if 0 <= edit1 < len(myEvent):
      editadd = input("What do you want to replace it with?\n")
      myEvent[edit1] = [editadd]
    else:
      print("Invalid item number.")
  except ValueError:
    print("Please enter a valid number.")
  time.sleep(2)
  os.system("clear")


def save_events():
  with open("Save.txt", "w") as r:
    r.write(str(myEvent))
  with open("Todo.txt", "w") as f:
    f.write(str(myEvent))


while True:
  answer = input(
      "Do you want to view, add, edit, clear, or remove an item from the to do list? \n"
  )
  if answer == "view":
    time.sleep(1)
    os.system("clear")
    view()
  elif answer == "add":
    time.sleep(1)
    os.system("clear")
    add = input("What do you want to add? \n")
    row = [add]
    myEvent.append(row)
    save_events()
  elif answer == "edit":
    time.sleep(1)
    os.system("clear")
    print("What do you want to edit?\n")
    view()
    edit()
    save_events()
  elif answer == "clear":
    myEvent = []
    save_events()
    print("The list has been cleared.")
  elif answer == "remove":
    criteria = input("What do you want to remove?: ").lower()
    myEvent = [row for row in myEvent if criteria not in row]
    save_events()
    print("Item removed.")
  else:
    print("Invalid option. Please choose view, add, edit, clear, or remove.")
  if fileExist:
    try:
      os.mkdir("backups")
    except:
      pass
      name = f"backup{random.randint(1,1000000000)}.txt"
      os.popen(f"cp to.do backups/{name}")
