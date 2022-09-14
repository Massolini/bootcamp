#Write your code below this line 👇
def paint_calc(height, width, cover):
    import math
    num_cans = ((test_h * test_w)/coverage)
    num_cans_rounded = math.ceil((test_h * test_w)/coverage)
    print(f"Total of paint you will need: {num_cans}")
    print(f"Number of cans you have to buy to paint it all: {num_cans_rounded}")






#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


