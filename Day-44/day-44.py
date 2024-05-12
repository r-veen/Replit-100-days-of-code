import random, time, os
print("Bingo!")
bingo = []
count = 1
def ran():
    number = random.randint(1,90)
    return number
def prettyprint():
    for j in bingo:
        for i in j:
            print(f"{i:^10}", end="  |  ")
        print("\n")
def createCard():
    global bingo
    numbers = []
    for i in range(8):
        numbers.append(ran())

    numbers.sort()

    bingo = [ [numbers[0], numbers[1],   numbers[2]],
              [numbers[3], "Bingo", numbers[4]],
              [numbers[5], numbers[6],   numbers[7]] 
            ]
createCard()
x = 1
while True:
    count +=1
    
    prettyprint()
    number = int(input("Next Number:  "))
    time.sleep(1)
    os.system("clear")
    for numbers in bingo:
        if number in numbers:
            index = numbers.index(number)
            numbers[index] = ("X")
            x += 1
    if x == 9:
        time.sleep(1)
        os.system("clear")
        break
print("You win")