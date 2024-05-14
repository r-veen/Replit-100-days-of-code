print("🌟MokeBeast Generator🌟")
beasts_list = []
def prettyprint():
    for beast in beasts_list:
        print(beast["name"]," |  ", beast["element"]," |  ", beast["move"]," |  ", beast["hp"]," |  ", beast["mp"]," |  ")

while True:
    name = input("Input the beast name > ").strip()
    element = input("Input the beast element > ").strip()
    move = input("Input the beast special move > ").strip()
    hp = input("Input the beast starting HP > ").strip()
    mp = input("Input the beast starting MP > ").strip()

    beast = {"name": name, "element": element, "move": move, "hp": hp, "mp": mp}
    beasts_list.append(beast)
    exit = input("Do you want to exit? > ").strip().lower()
    prettyprint()
    if exit == "yes":
        break