print ("Seja bem vindo a Montanha russa")
height = int(input("digite sua altura: "))

bill = 0

if height >= 120:
    print ("Altura apta a participar, ")
    age = int(input("Digite sua idade: "))
    if age < 12:
        bill += 5
        #print ("Sua tarifa é de $12")
    elif age <= 18:
        bill += 7
        #print ("sua tarifa é de $7")
    elif age >= 45 and age <= 55:
        print("Everething is going to be ok! enjoy your ride, its free")
    else:
        bill += 12
        #print ("sua tarifa é de $5")
        
    want_photos = input("Do you want a photo? Y or N: ")
    if want_photos == "Y" or want_photos == "y":
        bill += 3
    
    print(f"Sua tarifa é ${bill}")
        
        
else:
    print ("Nao atinge a altura necessaria para participar.")