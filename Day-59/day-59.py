print("🌟Palindrome Checker🌟")
word = input("Input a word > ").strip().lower()
backword = word[::-1]
if word == backword:
    print(f"Yes {word} is a palindrome")
else:
    print(f"No {word} is not a palindrome")