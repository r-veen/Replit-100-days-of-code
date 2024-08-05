print("Day 29 of 100 days of code. Replit", "\033[33m", end="")
print("\033[33m", sep="")

def newPrint(colour, word):
    if colour =="red":
        print("\033[31m",word, sep="", end="")
    elif colour =="yellow":
        print("\033[33m",word,sep="", end="")
    elif colour =="green":
        print("\033[32m",word,sep="", end="")
    elif colour =="blue":
        print("\033[34m",word,sep="", end="")
    else:
        print("\033[0m", word, sep="", end="")

print("Super Subroutine")
print("With my ", end="")
newPrint("red", "new program")
newPrint("reset", " I can just call red('and') ")
newPrint("red", "it will print in red ")
newPrint("blue", "or even blue") 