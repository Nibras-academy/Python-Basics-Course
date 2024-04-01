# Step 1: Ask the user to input the total number of students attending the event
total_students = int(input("Enter the total number of students attending the event: "))

# Step 2: Calculate the number of full rows
full_rows = total_students / 8

# Step 3: Calculate the number of students left over
students_leftover = total_students % 8

# Step 4: Print the results
print("Number of full rows:", full_rows)
print("Number of students left over:", students_leftover)


# Equal to
result = 10 == 5

# Not equal to
result = 20 != 8

# Greater than
result = 15 > 3

# Less than
result = 10 < 3

# Greater than or equal to
result = 8 >= 8

# Less than or equal to
result = 10 <= 3


# Assignment
x = 10

# Addition assignment
x += 5  # Equivalent to x = x + 5

# Subtraction assignment
x -= 3  # Equivalent to x = x - 3

# Multiplication assignment
x *= 2  # Equivalent to x = x * 2

# Division assignment
x /= 4  # Equivalent to x = x / 4




# Initialize total with an initial value of 100
total = 100

# Increment total by 50
total += 50

# Decrement total by 30
total -= 30

# Multiply total by 2
total *= 2

# Divide total by 3
total /= 3

# Print the final value of total
print("Final value of total:", total)




# Prompt the user to enter the length of the rectangle
length = float(input("Enter the length of the rectangle: "))

# Prompt the user to enter the width of the rectangle
width = float(input("Enter the width of the rectangle: "))

# Calculate the area of the rectangle
area = length * width

# Display the result
print("The area of the rectangle is:", area)
