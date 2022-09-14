# def greet(name):
    
#     print(f"\nWelcome {name} to Cipher program!\nWith this aplication you make your personal conversation safer!\n")

# greet("Mauro")
   
# Functions with more than 1 input
def greet_with (name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# If you switch the order it can put in the wrong place
# greet_with("Mauro", "Pamplona")

# to be at the correct location must have a keyword arguments / by using this you don´t have the problem of missplace by changin the order
greet_with(name="Mauro", location="Pamplona")
    