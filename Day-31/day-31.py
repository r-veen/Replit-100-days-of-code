
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
text = "="

newPrint("red", "=")
newPrint("white", "=")
newPrint("blue", "=")
music = "Music App"
newPrint("yellow", f"{music: >15}")
newPrint("red", "=")
newPrint("white", "=")
newPrint("blue", "=")
print()
print()
radio = "Radio Gaga"
print(f"{radio: >15}")
queen = "Queen"
print(f"{queen: >10}")