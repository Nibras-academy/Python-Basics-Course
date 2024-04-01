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


# Define the size of the square
size = 5

# Iterate over each row
for i in range(5):
    # For the first and last rows, or the first and last columns, print '*' for each column
    if i == 0 or i == 4:
        print('******')
    else:
        # For other rows, print '*' for the first and last columns, and spaces for the middle columns
        print('*    *')
        
        
# Define a string
text = "Hello"

# Loop over each character in the string
for char in text:
    print(char)
    
    
# Define the string
text = "Hello, world!"

# Initialize a variable to store the count
count = 0

# Loop over each character in the string
for char in text:
    # Increment the count for each character
    count += 1

# Print the total count of characters
print("Total number of characters:", count)


words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = 0

for word in words:
    if word == 'apple':
        word_counts += 1

print("Word counts:", word_counts)




#----------------------------------------------#

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
