student_name = input("Enter student name: ")

quiz_grade = float(input("Enter quiz grade: "))
mid_grade = float(input("Enter mid grade: "))
final_grade = float(input("Enter final grade: "))

total = quiz_grade + mid_grade + final_grade

print("Student Name:", student_name)
print("Total Grade:", total)

if total >= 60:
    print("Status: Pass")
else:
    print("Status: Fail")