print("Welcome to Python Pizza Deliveries!")
size = input("What size do you want? S, M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = 0

if size == "S" or "s":
    price = 15
elif size == "M" or "m":
    price = 20
elif size == "L" or "l":
    price = 25
else:
    print ("You do not choose the correct size, PLEASE INPUT: S, M OR L")
    
if add_pepperoni == "Y" or "y":
     if size == "S" or "s":
         price += 2
     else:
         price += 3
if extra_cheese == "Y" or "y":
     price += 1
print(f"Your final bill is: ${price}")


    
    