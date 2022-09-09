import random


word_list = ["ardvark", "baboom", "camel"]
words_in_list = len(word_list) #shows how many words contains in the list
random_word = random.randint(0, words_in_list -1) #chose one number from the quantity of words in the list -1 at the end because it goes from 0 to 2 and the total is +1 num
chosen_word = word_list[random_word] # shows whitch word was chosen by the number randomly chosed hehehe
chosen_word_list = list(chosen_word)
chosen_word_len = len(chosen_word)
#checking prints
#print(chosen_word_list)
# print(random_word)
print(chosen_word)
# print (len(chosen_word)) # testing print

play = input("Do you want to play Hangman? Type Y or N --> ").lower()


if play == "n":
    print("Bye!")
elif play == "y":
    print("Welcome to Hangman game! you have 5 try\'s before the man\'s die!\n")
    display = []
    for _ in chosen_word_list:
        display += "_"
    print(f"{display}")
    
    end_game = False
    while not end_game:
        
        guess = input("\nGuess a letter: --> ").lower()
    
    #create a loop that substitut the word in the display for the word in the chosen_word
        for position in range(chosen_word_len):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                print(display)
    
                    
            for letter in chosen_word_list:
                if letter == guess:
                    if display == chosen_word_list:
                        end_game = True
            
                else:
                    #print("Wrong!")
                
            
        
        
        
    
         
    
    

else:
    print("Please type Y or N to begin")
