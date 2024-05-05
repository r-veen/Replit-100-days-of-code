list = []
def name():
    firstname = input("What is your first name?\n").strip().capitalize()
    lastname = input("What is your last name?\n").strip().capitalize()

    if (firstname.strip().capitalize(), lastname.strip().capitalize()) not in list:
        list.append((firstname, lastname))
    else:
        print("You can't have it more than one time.")
    for i in range(len(list)):
        print(f"{list[i][0]} {list[i][1]}")
while True:
    name()