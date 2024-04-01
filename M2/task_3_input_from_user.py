# Prompt the user to enter the length and width of the rectangle
length_str = input("Enter the length of the rectangle: ")
width_str = input("Enter the width of the rectangle: ")

# Convert the input strings to floating-point numbers
length = float(length_str)
width = float(width_str)

# Calculate the area of the rectangle
area = length * width

# Display the calculated area to the user
print("The area of the rectangle is:", area)