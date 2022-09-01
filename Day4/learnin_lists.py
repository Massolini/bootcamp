#Lists initiate always with [ ]

provincias_de_espana = ["Álava","Navarra","La Rioja","Guipuzcoa"]

provincias_de_espana.append("Albacete") #(input("Digite el nombre de la provincia para añadirla: "))
provincias_de_espana.sort()

print(provincias_de_espana)

#append - adiciona um item no final da lista
# sort - classifica o modo que quer clasificar as informacoes
# https://docs.python.org/3/library/stdtypes.html#lists

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons" # quando adiciona -1 se lee de tras para frente comecando pelo -1
# fruits.append("Lemons")

# print(fruits) 



# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[0][1]) # o primeiro [] é para identificar se é fruta ou vegetal e o segundo [] é para os ingredientes