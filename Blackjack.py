from random import randint


def print_points(user, pc):
    print(f"Player points: {sum(user)}")
    print(f"AI points: {sum(pc)}")


user_cards = [randint(1, 10) for _ in range(2)]
comp_cards = [randint(1, 10) for _ in range(2)]
winpart = [18, 19, 20, 21]
takesCard = True

while takesCard:
    print(
        "Your cards are:",
        ", ".join(map(str, user_cards)),
        ": Total Points:",
        sum(user_cards),
    )
    print(f"AIs first card is {comp_cards[0]}")
    userinp = input("Wanna take a new card? y - Yes, n - No: ")
    print()
    if userinp == "y":
        user_cards.append(randint(1, 10))
        comp_cards.append(randint(1, 10))
    elif userinp == "n":
        takesCard = False
    else:
        print("Wrong choice y - Yes, n - No")

if sum(user_cards) in winpart and sum(comp_cards) not in winpart:
    print_points(user_cards, comp_cards)
    print("Player won!")
elif sum(comp_cards) in winpart and sum(user_cards) not in winpart:
    print_points(user_cards, comp_cards)
    print("AI won.")
elif sum(user_cards) == sum(comp_cards):
    print(f"Both player points are: {sum(comp_cards)}")
    print("It's a tie!")
else:
    if sum(user_cards) > sum(comp_cards):
        print_points(user_cards, comp_cards)
        print("Player won!")
    elif sum(user_cards) < sum(comp_cards):
        print_points(user_cards, comp_cards)
        print("AI won.")
