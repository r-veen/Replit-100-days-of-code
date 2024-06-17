def hangman():
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

def randomIdea():
    import random, os, time

    while True:
        f = open("my.idea", "a+")
        move = input("1 add idea\n2 see random idea? > ").strip().lower()
        
        if move == "1":
            idea = input("What do you want to add? > ").strip().lower()
            f.write(f"your idea is: {idea}\n")
            print("Nice, your idea has been stored.")
            time.sleep(3)
            os.system("clear")
        
        elif move == "2":
            f.seek(0)
            lines = f.readlines()
            if lines:
                random_line = random.choice(lines)
                print(random_line)
                time.sleep(3)
                os.system("clear")
            else:
                print("No ideas stored yet.")
                time.sleep(3)
                os.system("clear")
        f.close()
