# Step 1: Define the list of student names
students = ["Ali", "Khaled", "Ahmed"]


# Step 2: Define a list to store the grades of each student
grades = []

# Step 3: Nested loops to input grades for each student and subject
for student in students:
    # Temporary list to store grades for each student
    student_grades = []
   
    for subject in ["Math", "English", "Science"]:
        grade = float(input(f"Enter {subject} grade for {student}: "))
        student_grades.append(grade)
   
    # Add the grades for this student to the grades list
    grades.append(student_grades)
    
    
# Step 4: Calculate the average grade for each student
averages = []
counter = 0
for student_grades in grades:
    average_grade = sum(student_grades) / len(student_grades)
    print("Average grade for", students[counter], 'is: ', average_grade)
    counter += 1