print("🌟Factorial Finder🌟")
number = int(input("Input a number > "))
def factorial(value):
    if value <= 0:
        print("Done!")
        return 1
    else:
        result = 1
        for i in range(1, value + 1):
            result *= i
        print(f"The Factorial of {number} is {result}")
        return result
factorial(number)
