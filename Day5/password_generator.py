

# Password generator Project
import secrets
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
l2 = []
numbers = ['0', '1', '2', '3', '4', '5', '6' , '7', '8', '9']
symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', '\\', ':', ';', '"', '\'', '<', ',', '>', '.', '?', '/']

letters_upper = [letter.upper() for letter in letters] #generate a list of uppercase letters on the list letters
#print(letters_upper) 
l2 = letters + letters_upper # concatenate both letters un lowercase with letters in uppercase
#print(l2) 

print("Welcome to the PyPassword Generator!\n")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_numbers = int(input("How many numbers would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like in your password? \n"))

sr_letters = []
sr_numbers = []
sr_symbols = []

sr_letters = ''.join(secrets.choice(l2) for i in range(nr_letters))
sr_numbers = ''.join(secrets.choice(numbers) for i in range(nr_numbers))
sr_symbols = ''.join(secrets.choice(symbols) for i in range(nr_symbols))

# print(sr_letters)
# print(sr_numbers)
# print(f'{sr_symbols}\n')

combined = sr_letters + sr_numbers + sr_symbols

# print(f'{combined}\n')

shuffled_password = ''.join(random.sample(combined,len(combined)))

print(f'The Password sugestion is: --> {shuffled_password}')

    


