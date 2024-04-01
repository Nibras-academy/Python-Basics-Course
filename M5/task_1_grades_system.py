# ------Grades System---------#

# Ask the user to input the student's score
score = float(input("Enter the student's score: "))

# Check the score and determine the grade
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
    
# Print the student's grade
print("Student's Grade:", grade)
