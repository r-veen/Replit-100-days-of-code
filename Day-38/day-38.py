def newPrint(colour):
    if colour == "r":
        print("\033[31m", sep="", end="")
    elif colour == "y":
        print("\033[33m", sep="", end="")
    elif colour == "g":
        print("\033[32m", sep="", end="")
    elif colour == "b":
        print("\033[34m", sep="", end="")
    elif colour == " ":
        print("\033[0m", sep="", end="")

text = input("Gib einen beliebigen Satz ein:\n")
for letter in text:
    newPrint(letter.lower())
    print(letter, end="")
print()