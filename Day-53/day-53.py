import time, os
debugMode = False
row = []
inv = [row]

def save():
    f = open("inventory.txt", "w")
    f.write(str(inv))
    f.close

try:
    f = open("inventory.txt", "w")
    f.close()
except Exception as err:
    print("Error: Unable to load")
    if debugMode:
        print(err)

print("🌟RPG Inventory🌟")
while True:
    inp = input("1: add\n2: Remove\n3: View\n> ")
    if inp == "1":
        add = input("What do you wahnt to add? \n> ").strip().title()
        row.append(add)
        print(f"{add} has been added to your inventory.")
        time.sleep(2)
        os.system("clear")
        save()
    elif inp == "2":
        remove = input("What do you want to remove? \n> ").strip().title()
        if remove in row: 
            row.remove(remove)
            print(f"{remove} has been removed from your inventory.")
            time.sleep(2)
            os.system("clear")
        else:
            print("You don't have this in your inventory.")
            time.sleep(3)
            os.system("clear")
    elif inp == "3":
        view = input("Input the item to view\n> ").strip().title()
        if view in row:
            count = row.count(view)
            print(f"You have {count} {view}")
        else:
            print("You don't have this in your inventory.")
            time.sleep(3)
            os.system("clear")
    time.sleep(2)
    os.system("clear")
    save()

 