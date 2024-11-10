# Author: Wangoda Francis
# Registration number: 24/U/11855/PS

# ===== Student Information Input =====
# Get student's personal details
student_name = input("Enter your name: ")
student_number = input("Enter your student number: ")

# Initialize empty lists to store course information
student_marks = []    # Will store marks for each course
credit_units = []     # Will store credit units for each course

# ===== Course Marks Input =====
# Loop to get marks for 4 courses
for i in range(1, 5):
    marks = int(input(f"Enter marks for course {i}: "))
    student_marks.append(marks)

# ===== Credit Units Input =====
# Loop to get credit units for 4 courses
for i in range(1, 5):
    units = int(input(f"Enter credit unit for course {i}: "))
    credit_units.append(units)


# ===== Grade Conversion Function =====
def convert_marks_to_grades(student_marks):
    """
    Converts numerical marks to letter grades
    Args:
        student_marks (int): Numerical marks (0-100)
    Returns:
        str: Letter grade (A, B, C, D, E, or F)
    """
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


# ===== CGPA Calculation Function =====
def calculate_cgpa(student_marks, credit_units):
    """
    Calculates the CGPA based on marks and credit units
    Args:
        student_marks (list): List of marks for each course
        credit_units (list): List of credit units for each course
    Returns:
        float: Calculated CGPA
    """
    # Define grade points for each letter grade
    grade_points = {
        'A': 5,  # 90-100
        'B': 4,  # 80-89
        'C': 3,  # 70-79
        'D': 2,  # 60-69
        'E': 1,  # 50-59
        'F': 0,  # Below 50
    }
    
    # Initialize accumulators
    total_grade_points = 0    # Sum of (grade points × credit units)
    total_credit_units = 0    # Sum of all credit units

    # Calculate weighted grade points for each course
    for i in range(len(student_marks)):
        mark = student_marks[i]
        credit_unit = credit_units[i]

        # Convert marks to grade, then to grade points
        grade = convert_marks_to_grades(mark)
        grade_point = grade_points[grade]

        # Accumulate weighted grade points and credit units
        total_grade_points += (grade_point * credit_unit)
        total_credit_units += credit_unit

    # Prevent division by zero
    if total_credit_units == 0:
        return 0

    # Calculate final CGPA
    cgpa = total_grade_points / total_credit_units
    return cgpa


# ===== Main Execution =====
# Calculate CGPA and display result
cgpa = calculate_cgpa(student_marks, credit_units)
print(f"The CGPA for {student_name} is: {cgpa: .2f}")


