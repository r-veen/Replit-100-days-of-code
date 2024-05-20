import os, time

f = open("high.score", "a+")
while True:
    initial = input("Input your initials > ").strip()
    while len(initial) != 3:
        initial = input("Needs to be 3 letters > ").strip()
    score = int(input("Input your score > "))
    while score > 100000 or score < 1:
        score = int(input("It needs to be a positive number and under 100000"))
    f.write(f"Initial: {initial}\nScore:{score}\n")
    exit = input("Exit? > ").strip().lower()
    if exit == "yes":
        break
    time.sleep(2)
    os.system("clear")
p = f.read()
print(p)
f.close()