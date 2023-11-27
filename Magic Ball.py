from random import *

answers = [
    "Sure!",
    "I guess so.",
    "It's unclear. Try one more time.",
    "Don't you dare.",
    "Amen.",
    "I guess so.",
    "Ask me later.",
    "I'm saying no,",
    "No doubt.",
    "Good chances.",
    "You better not.",
    "No!",
    "You can be sure.",
    "Yes.",
    "Concentrate and ask once again.",
    "Very suspicious.",
]
print("YoHo! I am the magic ball and I can answer all of your questions!")
print("What's your name?:")
name = input()
print(f"Hello, {name}")
while True:
    print("What do you wnat to ask?")
    answer = input()
    print(choice(answers))
    print("Anything else?")
    answer2 = input()
    if answer2 in "yes":
        continue
    else:
        print("Come back soon!")
        break
