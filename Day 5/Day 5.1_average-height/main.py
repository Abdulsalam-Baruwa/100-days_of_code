student_heights = input("Input a list of student heights \n").split()
total_height = 0
num_of_students = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    total_height += student_heights[n]
    num_of_students += 1
print(student_heights)
average_height = round(total_height / num_of_students)
print(f"The average height is: {average_height}")