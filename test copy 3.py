# Using three single quotes for multi-line strings
multi_line_string = '''
This is a multi-line
string that spans
multiple lines
'''
print(multi_line_string)


# # Attempting to include quotes within a string
# sentence = "He said, "I can't do it.""


# Using different quotes or escape characters
sentence = "He said, 'I can't do it.'"  # Using single quotes outside double quotes
sentence = 'He said, "I can\'t do it."'  # Using escape character (\) before the single quote


# Multiplying strings
stars = "*" * 10
print(stars)


# Indexing strings
word = "Python"
print(word[0])  # Output: P
print(word[-1])  # Output: n (negative indexing starts from the end)


# Slicing strings
word = "Python"
print(word[0:3])  # Output: Pyt (from index 0 to 2, excluding 3)
print(word[2:])   # Output: thon (from index 2 to the end)









coordinates = (10, 20)
print(coordinates[0])  # Output: 10


# Define a tuple to store student information
student_info = ("Adel", 18, "A")

# Accessing elements from the tuple
print("Student name:", student_info[0])
print("Student age:", student_info[1])
print("Student grade:", student_info[2])

# Finding the length of the tuple
print("Length of the tuple:", len(student_info))


# Concatenation
additional_info = ("Mathematics", "Science")
full_student_info = student_info + additional_info
print("Full student information:", full_student_info)

# Repetition
repeated_info = ("High",) * 3
print("Repeated information:", repeated_info)
