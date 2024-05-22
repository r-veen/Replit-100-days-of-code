import random, os, time

while True:
    f = open("my.idea", "a+")
    move = input("1 add idea\n2 see random idea? > ").strip().lower()
    
    if move == "1":
        idea = input("What do you want to add? > ").strip().lower()
        f.write(f"your idea is: {idea}\n")
        print("Nice, your idea has been stored.")
        time.sleep(3)
        os.system("clear")
    
    elif move == "2":
        f.seek(0)
        lines = f.readlines()
        if lines:
            random_line = random.choice(lines)
            print(random_line)
            time.sleep(3)
            os.system("clear")
        else:
            print("No ideas stored yet.")
            time.sleep(3)
            os.system("clear")
    f.close()
