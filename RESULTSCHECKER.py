Students = []
Students.append(("favour", (90 , 89 , 95)))
Students.append(("jayden", (90 , 89 , 95)))
Students.append(("munachi", (90 , 89 , 95)))
# Student Grade Tracker

students = []

# Add students
students.append(("Emma", (70, 85, 90)))
students.append(("John", (60, 75, 80)))
students.append(("Grace", (88, 92, 95)))

# Display all student records
print("STUDENT RECORDS")
print("-" * 30)

for student in students:
    name = student[0]
    grades = student[1]

    average = sum(grades) / len(grades)

    print(f"Name: {name}")
    print(f"Grades: {grades}")
    print(f"Average Score: {average:.2f}")
    print("-" * 30)

# Find highest average
highest_student = max(
    students,
    key=lambda s: sum(s[1]) / len(s[1])
)

# Find lowest average
lowest_student = min(
    students,
    key=lambda s: sum(s[1]) / len(s[1])
)

print("\nTOP STUDENT")
print(highest_student[0])

print("\nLOWEST STUDENT")
print(lowest_student[0])
