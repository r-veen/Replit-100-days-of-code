import time, os

print("🌟Life Organizer🌟")
time.sleep(2)
os.system("clear")
print()
todo = []
pList = []


def prettyprint():
    for i in todo:
        for j in i:
            print(j, end=" | ")
        print("\n")


def add():
    task = input("What is the task? > ").strip().lower()
    due = input("When is it due by? > ").strip().lower()
    priority = input("What is the priority? > ").strip().lower()
    pList.append(priority)
    print()
    entry = [task, due, priority]
    print(f"Thanks, {task} has been added.")
    time.sleep(2)
    os.system("clear")
    todo.append(entry)


def view():
    choice = input(
        "Do you want to see all or a certain group? > ").strip().lower()
    time.sleep(1)
    os.system("clear")
    if choice == "all":
        prettyprint()
    else:
        group = input("Which group do you want to access? > ").strip().lower()
        if group in pList:
            for item in todo:
                if item[2] == group:
                    print(item[0], item[1], item[2], sep=' | ')
        else:
            print("You don't have that in your list")
            time.sleep(2)
            os.system("clear")


def edit():
    task = input("What task do you want to edit? > ").strip().lower()
    for i, item in enumerate(todo):
        if task in item:
            new_value = input(
                "What do you want to change it to? > ").strip().lower()
            item[0] = new_value
            print("Task updated.")
            time.sleep(2)
            os.system("clear")
            break
    else:
        print("This task is not in your list.")


def remove():
    task = input("What task do you want to remove? > ").strip().lower()
    for item in todo:
        if task in item:
            todo.remove(item)
            print("Task removed.")
            break
    else:
        print("That task is not in your list.")


while True:
    action = input(
        "Welcome to the Life Organizer. Do you want to add, view, edit, or remove a to-do? > "
    ).strip().lower()
    if action == "add":
        add()
    elif action == "view":
        view()
    elif action == "edit":
        edit()
    elif action == "remove":
        remove()
    exit = input("Do you wahnt to exit? > ").strip().lower()
    time.sleep(2)
    os.system("clear")
    if exit == "yes":
        break
