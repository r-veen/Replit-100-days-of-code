import random
print("Hangman Game!")
lives = 5
listWords = ["apple", "animal", "emerald", "fish", "carrot", "cable", "computer", "night", "unicorn", "salad"]
word = random.choice(listWords)
sWords = ['_' for _ in word]

def work(guess):
    global lives 
    if guess not in word:
        print(f"no {guess} was not in the word. You have {lives} left")
        lives -= 1 
    for index, letter in enumerate(word):
        if letter == guess:
            sWords[index] = guess 

while lives > 0:
    print(' '.join(sWords))
    guess = input("Guess a letter: ").strip().lower()
    work(guess)
    if '_' not in sWords:
        print("Congratulations, you've guessed the word!")
        print(f"You still had {lives} left.")
        break

if lives == -1:
    print("You have failed. The word was:", word)
