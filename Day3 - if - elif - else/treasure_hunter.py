print("Welcome to Treasure Hunting.\n")
print("Your mission is to find the treasure.\n")

choice1 = input('You entered inside the Great Piramid and it has an huge corridor where you have to choose between two routes.. whitch one do you take? "left" or "right": --> ').lower()

if choice1 == "left":
    choice2 = input('You\'ve chosen the right path and crossed some fabulouse artifacts on the way but now you have to take another dificult decision, in front of you have a enourmous rock and have space to pass "Over" it or "Under" it, whitch one you chose? -->').lower()
    if choice2 == "under":
        choice3 = input('You are very lucky fellow the rock was safe to go under and did not fall over you, but after it you have encounter three paths and have to decide whitch one you take: "right", "straight" or "left": -->').lower()
        if choice3 == "straight":
            print("You reached the treasure room and faound an incredible amount of jewels and gold artifacts you are rich!! well done")
        elif choice3 == "right":
            print("The path you chose had too many traps and you died in one of them... Game over")
        else:
            print("On the left path you found the exit of the piramid but the light was so bright that you did not see the edge and fell from the top of the piramid... Game over.")   
    else:
        print("While passing over the rock it moved because your weight and roll over you and you did not survive... Game over")
else:
    print("You\'ve felt into a trap and died.. Game over")
    