import random
from hangman_art import logo, stages #separated from coma you can add the second import from the same file
from hangman_words import word_list

#word_list = ["ardvark", "baboon", "camel"]
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

print(logo)
play = input("Do you want to play Hangman? Type Y or N --> ").lower()


if play == "n":
    print("Bye!")
elif play == "y":
    print("Welcome to Hangman game! you have 6 try\'s before the man\'s die!\n")
    print(stages[6])
    
    display = []
    for _ in chosen_word_list:
        display += "_"
    print(f"{display}")
    
    end_game = False
    lives = 6
    
    while not end_game:
        
        guess = input("\nGuess a letter: --> ").lower()

        if guess in display:
            print(f"The letter \"{guess}\" was already chosen, pick another one!")
            
        #create a loop that substitut the word in the display for the word in the chosen_word
        for position in range(chosen_word_len):
            letter = chosen_word[position]
            #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter
        print(display)
    
        if "_" not in display: #check if the game finish and user won and also end the While loop
            end_game = True
            print("You win")      
        
        
            
        if guess not in chosen_word:
            print(f"You guess wrong")
            lives -= 1
            print(stages[lives])
            print(f"Careful you have only {lives} lives left")
            
            if lives == 0: 
                print("End of lives, You lose")
                end_game = True
            
        
        
            
                
else:
    print("Please type Y or N to begin otherwise the game does not start")
