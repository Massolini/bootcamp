from calendar import c


row1 = ["#","#","#"]
row2 = ["#","#","#"]
row3 = ["#","#","#"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")  # se utiliza o \n para separar cada linha e deixar uma embaixo da outra  \n se usa para nova linha
position = input("Where do you want to put the treasure? ") # 23 = column 2, row 3 

column = int(position[0]) # vai selecionar o primeiro caracter e transformarlo em int
row = int(position[1]) # vai selecionar o segundo caracter e transformarlo em int

select_row = map[row -1]
select_row [column -1] = "X"

#  map[row -1][column -1] = "X" # This also works as it shoud


print(f"{row1}\n{row2}\n{row3}")