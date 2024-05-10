import random
print("Bingo card generator")
bingo = []
def ran():
    number = random.randint(1,90)
    return number

def prettyprint():
    for j in bingo:
        print(j)

numbers = []
for i in range(8):
    numbers.append(ran())

numbers.sort()

bingo = [ [numbers[0], numbers[1], numbers[2]],
          [numbers[3], "Bingo",    numbers[4]],
          [numbers[5], numbers[6], numbers[7]]
        ]
prettyprint()