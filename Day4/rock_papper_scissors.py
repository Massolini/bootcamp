import random

user_choice = int(input("\nLet\'s play Rock, Papper and Scissors!\nType 0 for Rock, 1 for Papper, 2 for Scissors.\nWhat do you choose? --> "))

oponent_choice = random.randint(0,2)

print(f"\nPlayer choice: {user_choice} >< Computer choice: {oponent_choice}\n" )

if user_choice == 0 and oponent_choice == 0:
    print("It\'s a draw! everebody wins :)\n")
elif user_choice == 0 and oponent_choice == 1:
    print("Paper wraps rock. Computer win!\n")
elif user_choice == 0 and oponent_choice == 2:
    print("Rock crushes scissors! You win!\n")
elif user_choice == 1 and oponent_choice == 0:
    print("Paper wraps rock. You win!\n")
elif user_choice == 1 and oponent_choice == 1:
    print("It\'s a draw! everebody wins :)\n")
elif user_choice == 1 and oponent_choice == 2:
    print("Scissors cuts paper! Computer win!\n")
elif user_choice == 2 and oponent_choice == 0:
    print("Rock crushes scissors! Computer win!\n")
elif user_choice == 2 and oponent_choice == 1:
    print("Scissors cuts paper! You win!\n")
elif user_choice == 2 and oponent_choice == 2:
    print("It\'s a draw! everebody wins :)\n")
else:
    print("chose a number betwen 0, 1 or 2\n")
