
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
newPrint("red", "=")
newPrint("white", "=")
newPrint("blue", "=")
newPrint("yellow", "Music App")
newPrint("red", "=")
newPrint("white", "=")
newPrint("blue", "=")