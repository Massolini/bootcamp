year = int(input("Digite um ano: "))

if year % 4 == 0:
    if year % 100 == 1:
        print ("O ano " + str(year) + " é ano bisexto.")
    elif year % 400 == 0:
        print ("O ano " + str(year) + " é ano bisexto.")
    else:
        print ("O ano " + str(year) + " nao é ano bisexto.") 
else:
    print ("O ano " + str(year) + " nao é ano bisexto.")  
    