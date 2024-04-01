# ------Calculator---------#

# Welcome message
print("Welcome To The Calculator!")

# Input for the first number
num1 = float(input("Enter the first number: "))

# Input for the operation
operation = input("Enter the operation (+, -, *, /): ")

# Input for the second number
num2 = float(input("Enter the second number: "))


# Perform the operation based on user input
if operation == '+':
    result = num1 + num2
    print("Result:", result)
elif operation == '-':
    result = num1 - num2
    print("Result:", result)
elif operation == '*':
    result = num1 * num2
    print("Result:", result)
elif operation == '/':
    result = num1 / num2
    print("Result:", result)

else:
    print("Invalid operation. Please enter a valid operation.")

# Thank you message
print("Thank you for using the Guided Calculator!")

