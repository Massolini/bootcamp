print ("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your name? \n")

lowerName1 = name1.lower()
lowerName2 = name2.lower()
concatenateNames = lowerName1 + lowerName2

t = concatenateNames.count("t")
r = concatenateNames.count("r")
u = concatenateNames.count("u")
e = concatenateNames.count("e")

trueScore = t + r + u + e

l = concatenateNames.count("l")
o = concatenateNames.count("o")
v = concatenateNames.count("v")
e = concatenateNames.count("e")

loveScore = l + o + v + e

totalScore = int(str(trueScore) + str(loveScore))

if totalScore < 10 or totalScore > 90:
    print(f"Your score is {totalScore}, you go together like coke and mentos.")
elif totalScore >= 40 and totalScore <= 50:
    print(f"Your score is {totalScore}, you are alright together.")
else:
    print(f"Your score is {totalScore}")

