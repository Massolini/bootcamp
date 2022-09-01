import random
names_string = ("Mauro, Marcia, Rui, Rosane, Simone")# input("Give me everybody\'s names, seperated by a comma: ")
names = names_string.split(",")
numero_de_pessoas = len(names) - 1 
# O -1 para é nao passar do range ex. se o numero da lista sao 5 pessoas a lista conta de zero 0 a quatro 4 sem o -1 apareceria o 5 e da erro por nao existir na lista

random_choice = random.randint(0, numero_de_pessoas)

print(random_choice) #mostra o numero da lista gerado

print(f"O nome escolhido para pagar a conta é: {names[random_choice]}")