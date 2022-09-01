import random

user_choice = input("What do you choose? Type 0 for Rock, 1 for Papper, 2 for Scissors.")

oponent_choice = random.randint(0,2)

if user_choice == 0 and oponent_choice == 0:
    print