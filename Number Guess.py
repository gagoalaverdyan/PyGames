from random import *


def is_valid(num):
    if num in range(0, 101):
        return True
    else:
        return False


print("Welcome to number guess!")
print("Set the range for random number:")
num = randint(1, int(input()))
number_of_guesses = 0
while True:
    print("Enter a number:")
    guess = int(input())
    if not is_valid(guess):
        print("The number must be in the range of 1 to 100.")
    else:
        if guess == num:
            print("That's it!")
            print(f"It took you {number_of_guesses} tries")
            print("Thanks for playing! See you.")
            break
        elif guess < num:
            print("The entered number is smaller. Try gain.")
            number_of_guesses += 1
        elif guess > num:
            print("The entered number is larger. Try gain.")
            number_of_guesses += 1
