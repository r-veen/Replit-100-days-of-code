import random
print("Hangman Game!")
print(" +---+\n", "|   |\n", "    |\n", "    |\n", "    |\n", "    |\n", )
print()
lives = 6
listWords = ["apple", "animal", "emerald", "fish", "carrot", "cable", "computer", "night", "unicorn", "salad"]
word = random.choice(listWords)
sWords = ['_' for _ in word]

def work(guess):
    global lives 
    if guess not in word:
        print(f"no {guess} was not in the word.")
        lives -= 1 
        if lives == 5:
            print(" +---+\n", "|   |\n", "o   |\n", "    |\n", "    |\n", "    |\n", )
        elif lives == 4:
            print(" +---+\n", "|   |\n", "o   |\n", "|   |\n", "    |\n", "    |\n", )
        elif lives == 3:
            print("  +---+\n", " |   |\n", " o   |\n", "/|   |\n", "     |\n", "     |\n", )
        elif lives == 2:
            print("  +---+\n", " |   |\n", " o   |\n", "/|\  |\n", "     |\n", "     |\n", )
        elif lives == 1:
            print("  +---+\n", " |   |\n", " o   |\n", "/|\  |\n", "/    |\n", "     |\n", )
        elif lives == 0:
            print("  +---+\n", " |   |\n", " o   |\n", "/|\  |\n", "/ \  |\n", "     |\n", )
    for index, letter in enumerate(word):
        if letter == guess:
            sWords[index] = guess 

while lives > 0:
    print(' '.join(sWords))
    guess = input("Guess a letter: ").strip().lower()
    if guess in sWords:
        print("You already had this letter")
    work(guess)
    if '_' not in sWords:
        print("Congratulations, you've guessed the word!")
        print()
        break

if lives == 0:
    print("You have failed. The word was:", word)

