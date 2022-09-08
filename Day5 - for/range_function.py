#for loop with range
#for number in range(1, 11, 3):
#   print(number)

# total = 0 
# for number in range(1, 101):
#     total += number
# print(total)

#The code bellow will sum the "even" (numeros pares) numbers in the range of 1 to 101
total = 0
for number in range(2, 101, 2):
    total += number 
print(total)

total2 = 0 
for number in range(2, 101):
    if number % 2 == 0: # esta formula mostra os numeros pares
        total2 += number
print(total2)