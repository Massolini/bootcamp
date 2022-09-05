students_scores = ("78 65 89 86 55 91 64 89").split() # input("Input a list of students scores: ")
for n in range(0 , len(students_scores)):
    students_scores[n] = int(students_scores[n])
print(students_scores)

max_score = 0 
for score in students_scores:
    if score > max_score:
        max_score = score
print (f"The highest score in the class is: {max_score}")