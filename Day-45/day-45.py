print("🌟Life Organizer🌟")
print()
todo = []

def prettyprint():
    for i in todo:
        for j in i:
            print(j, end=" | ")
while True:
    input1 = input("Welcome to the life organizer. Do you want to add, view, edit or remove a to do? > ").strip().lower()
    if input1 == "add":
        add1 = input("What is the task? > ")
        due = input("When is it due by? > ")
        priority = input("What is the priority? > ")
        print()
        add = [add1, due, priority]
        print(f"Thanks, {add1} has been added.")
        todo.append(add)
    elif input1 == "view":
        prettyprint()