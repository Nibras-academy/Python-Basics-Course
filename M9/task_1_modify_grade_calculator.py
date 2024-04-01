
# Function to input grades for each subject
def calc_grades():
    math_grade = float(input("Enter Math grade: "))
    english_grade = float(input("Enter English grade: "))
    science_grade = float(input("Enter Science grade: "))
    total_grades = math_grade + english_grade + science_grade
    average_grade = total_grades / 3
    return average_grade



average = calc_grades()
print("Average grade:", average)

