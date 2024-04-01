#------------Grades Checker------------------#

# Prompt the user to enter a list of grades separated by spaces
grade_list = input("Enter a list of grades separated by spaces: ")

# Split the input string into individual grades
grades = grade_list.split()

# Initialize counter variables for passed and failed students
passed_count = 0
failed_count = 0

# Iterate over each grade in the list
for grade in grades:
    # Convert the grade from string to integer
    grade = int(grade)
    
    # Check if the grade is greater than or equal to 50 (passing grade)
    if grade >= 50:
        # Increment the passed count if the grade is passing
        passed_count += 1
    else:
        # Increment the failed count if the grade is failing
        failed_count += 1

# Print the total counts of passed and failed students
print("Total passed students:", passed_count)
print("Total failed students:", failed_count)
