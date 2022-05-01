from turtle import st


student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# Create an empty dictionary called student_grades
student_grades = {}
# Add the grades to student_grades
#student_grades["Harry"] = "Exceeds Expectations"
#student_grades["Ron"] = "Acceptable"
#student_grades["Hermione"] = "Outstanding"
#student_grades["Draco"] = "Acceptable"
#student_grades["Neville"] = "Fail"
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80 and score < 90:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70 and score < 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)