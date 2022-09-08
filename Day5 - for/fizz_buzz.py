# numbers = range(1,100):
# for n in numbers:
#     # for n in intnumbers: 
#     #     if n %3 == 0:
#     #         n = "fizz"
#     #     elif n %5 == 0:
#     #         n = "buzz"
#     #     elif n %3 == 0 and n %5 == 0:
#     #         n = "FizzBuzz"
#     print(numbers)  

# for numbers in range(1,101):
#     numbers[n] = int(numbers[n])
    
#     for n in numbers:
#         if numbers %3 == 0:
#             n = 99
#     print (numbers)

#correct answer

for number in range(1, 101):
    if number %3 == 0 and number %5 == 0:
        print("FizzBuzz")
    elif number %5 == 0:
        print("Buzz")
    elif number %3 == 0:
        print("Fizz")
    else:
        print(number)