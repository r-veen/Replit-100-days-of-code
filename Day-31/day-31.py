def newPrint(colour, word):
    if colour =="red":
        print("\033[31m",word, sep="", end="")
    elif colour =="yellow":
        print("\033[33m",word,sep="", end="")
    elif colour =="green":
        print("\033[32m",word,sep="", end="")
    elif colour =="blue":
        print("\033[34m",word,sep="", end="")
    elif colour == "white":
        print("\033[0m", word, sep="", end="")
text = '='
newPrint("red", f"{text: >15}")
newPrint("white", "=")
newPrint("blue", "=")
newPrint("yellow", "Music App")
newPrint("red", "=")
newPrint("white", "=")
newPrint("blue", "=")
print()
radio = "Radio Gaga"
newPrint("white",f"{radio: >20}")
newPrint("yellow","")
print()
queen = "Queen"
print(f"{queen: >15}")
print()
newPrint("white", "Prev")
print()
next = "Next"
newPrint("green",f"{next: >10}")
print()
pause = "\033[38;5;201mPause"
print(f"{pause: >28}")
print()
print()
title = "Welcome to"
newPrint("white",f"{title: >20}")
print()
line = "--"
newPrint("blue",f"{line: >5}")
title2 = "ARMBOOK"
print(f"{title2: >10}",end="")
print(f"{line: >5}")
print()
text1 = "Definitely not a rip off of a certain other social networking site."
newPrint("yellow",f"{text1: >70}")
print()
print()
print()
text3 = "Honest."
newPrint("red",f"{text3: >10}")
name = "Username:"
password = "Password:"
print()
print()
newPrint("white",f"{name: >12}")
print()
newPrint("white",f"{password: >12}")