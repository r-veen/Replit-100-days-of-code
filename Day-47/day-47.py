import random, time, os

def prettyprint():
    for key, value in trumps.items():
        print(key)

trumps = {}
trumps["David"] = {"Intelligence": 178, "Speed": 4, "Guile": 80, "Baldness": 99}
trumps["Mr Spock"] = {"Intelligence": 200, "Speed": 50, "Guile": 50, "Baldness": 0}
trumps["Moica from Friends"] = {"Intelligence": 150, "Speed": 50, "Guile": 50, "Baldness": 0}
trumps["Professor X"] = {"Intelligence": 250, "Speed": 1, "Guile": 200, "Baldness": 101}

while True:
    print("🌟Top Trumps🌟")
    print("----------------")
    print()
    print("Welcome to the Top Trumps 'Most Handsome Computing Teachers' Simulator")
    print("Characters: ")
    prettyprint()
    time.sleep(4)
    os.system("clear")
    pick = input("Pick your character \n> ").strip().title()

    full_names = [full_name for full_name in trumps.keys()]
    choice = random.choice(list(trumps.keys()))

    print(f"Computer has picked {choice}")
    time.sleep(2)
    os.system("clear")
    stat = input("Choose your stat: Intelligence, Speed, Guile and Baldness Level \n> ").strip().title()
    user_stat = trumps[pick].get(stat.capitalize(), None)
    computer_stat = trumps[choice].get(stat.capitalize(), None)

    if user_stat is not None and computer_stat is not None:
        if user_stat > computer_stat:
            print(f"{pick} has won this round!")
            time.sleep(3)
            os.system("clear")
        elif user_stat < computer_stat:
            print(f"{choice} has won this round!")
            time.sleep(3)
            os.system("clear")
        else:
            print("It's a tie!")
            time.sleep(3)
            os.system("clear")
    else:
        print("An error occurred with the stat selection. Please try again.")
        time.sleep(3)
        os.system("clear")
    exit = input("Exit?\n> ")
    if exit == "yes":
        break