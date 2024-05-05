import os, time

print("To Do List Manager: ")
print()
list = []


def view():
    for j in range(len(list)):
        print(f"{list[j]}\n")


def edit():
    edit1 = int(input("Which number?"))
    if edit1 < len(list):
        editadd = input("What do you want to replace it with?\n")
        list.pop(edit1)
        list.insert(edit1, editadd)
    else:
        print("Invalid item number.")
    time.sleep(2)
    os.system("clear")


while True:
    answer = input(
        "Do you want to view, add, edit, erase, or remove an item from the to do list? \n"
    )
    if answer == "view":
        time.sleep(1)
        os.system("clear")
        view()
    elif answer == "add":
        
        time.sleep(1)
        os.system("clear")
        add = input("What do you wahnt to add? \n")
        if add in list:
            print("You cant have it two times in your list!")
        else:
            list.append(add)
    elif answer == "edit":
        time.sleep(1)
        os.system("clear")
        print("What do you wahnt to edit?\n")
        for i in range(len(list)):
            print(f"{i}: {list[i]}")
        i == 0
        edit()
    elif answer == "erase":
        list.clear()
    elif answer == "remove":
        if len(list) > 0:
            print("Current list items:")
            for i in range(len(list)):
                print(f"{i}: {list[i]}")
            remove = input("What do you want to remove? Please type the exact content: \n")
            if remove in list:
                list.remove(remove)
                print("Item removed.")
            else:
                print("This item is not in your list.")
        else:
            print("The list is currently empty.")
