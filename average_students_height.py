student_heights = ("156 178 165 171 187").split() # input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

number_of_sutdents = 0
for students in student_heights:
    number_of_sutdents += 1
print(number_of_sutdents)

average_height = total_height / number_of_sutdents

print (round(average_height))