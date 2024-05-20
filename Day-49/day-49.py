import os, time

def prettyprint(lines):
    for line in lines:
        print(line.strip())
        time.sleep(1)

f = open("high.score", "a+")
while True:
    initial = input("Input your initials > ").strip()
    while len(initial) != 3:
        initial = input("Needs to be 3 letters > ").strip()
    score = int(input("Input your score > "))
    while score > 100000 or score < 1:
        score = int(input("It needs to be a positive number and under 100000"))
    f.write(f"Initial: {initial}\nScore: {score}\n")
    exit = input("Exit? > ").strip().lower()
    if exit == "yes":
        break
    time.sleep(2)
    os.system("clear")
f.close()

f = open("high.score", "r")
lines = f.readlines()
f.close()

if len(lines) % 2 != 0:
    print("Die Anzahl der Zeilen ist ungerade. Bitte überprüfe die Datei.")
    exit()

highest_score = 0
winner_initial = ""

for i in range(0, len(lines), 2):
    initial = lines[i].split(":")[1].strip()
    score = int(lines[i+1].split(":")[1].strip())
    
    if score > highest_score:
        highest_score = score
        winner_initial = initial

print(f"Winner: {winner_initial} with a score of {highest_score}")
prettyprint(lines)