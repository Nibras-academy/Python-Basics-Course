print("Hello, world!")
print("Hello, world!")
print("Hello, world!")
print("Hello, world!")
print("Hello, world!")
print("----------")

for i in range(5):
    print("Hello, world!")


# Example: Printing numbers from 1 to 5 using a for loop
for num in range(1, 6):  # Initialization and iterable
    print(num)            # Loop body


for i in range(5):
    print(i)

for i in range(0, 5):
    print(i)

for i in range(1, 10, 2):
    print(i)



        


words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = 0

for word in words:
    if word == 'apple':
        word_counts += 1

print("Word counts:", word_counts)




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
