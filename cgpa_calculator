# My Name is Wangoda Francis
# Registration number is 24/U/11855/PS

# Getting student details
student_name = input("Enter your name: ")
student_number = input("Enter your student number: ")

# creating lists for student marks and credit units
student_marks = []
credit_units = []

# Getting student marks
for i in range(1, 5):
    marks = int(input(f"Enter marks for course {i}: "))
    student_marks.append(marks)

# Getting the credit units of the students
for i in range(1, 5):
    units = int(input(f"Enter credit unit for course {i}: "))
    credit_units.append(units)


# Function to convert marks into grades
def convert_marks_to_grades(student_marks):
    if student_marks >= 90:
        return "A"
    elif student_marks >= 80:
        return "B"
    elif student_marks >= 70:
        return "C"
    elif student_marks >= 60:
        return "D"
    elif student_marks >= 50:
        return "E"
    else:
        return "F"


# Calculating the CGPA
def calculate_cgpa(student_marks, credit_units):
    # Dictionary for assigning grade points to each grade
    grade_points = {
        'A': 5,
        'B': 4,
        'C': 3,
        'D': 2,
        'E': 1,
        'F': 0,
    }
    total_grade_points = 0
    total_credit_units = 0

    # loop through the marks and corresponding credit units
    for i in range(len(student_marks)):
        mark = student_marks[i]
        credit_unit = credit_units[i]

        # convert the marks to grades and Convert the grades to grade points
        grade = convert_marks_to_grades(mark)
        grade_point = grade_points[grade]

        # accumulating the credit units and grade points
        total_grade_points = total_grade_points + (grade_point * credit_unit)
        total_credit_units = total_credit_units + credit_unit

    # calculate the CGPA
    if total_credit_units == 0:
        return 0      # this is to avoid the division by zero

    cgpa = total_grade_points / total_credit_units
    return cgpa


# Calculate and display the CGPA
cgpa = calculate_cgpa(student_marks, credit_units)
print(f"The CGPA for {student_name} is: {cgpa: .2f}")


