age = 25
if age > 20:
    print("You are too old!")
else:
    print("You are not too old!")


age = 18
if age >= 20:
    print("You are too old!")
elif age < 20 and age >= 13:
    print("You are a teenager!")
else:
    print("You are young!")


# Define a variable
x = 10

# Check if x is greater than 5
if x > 5:
    # This block of code will execute if the condition is True
    print("x is greater than 5")
    print("This statement is also inside the if block")

# This statement is outside the if block
print("End of program")



# Define a variable
x = 10

# Check if x is greater than 5
if x > 5:
    # This block of code will execute if the condition is True
    print("x is greater than 5")
    print("This statement is also inside the if block")
    x += 1  # Increment x by 1
    print("Now x is:", x)

# This statement is outside the if block
print("End of program")



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


print(num1 + num2)



# Example of logical operators
x = 5
y = 10

# Using 'and' operator
if x > 0 and y < 15:
    print("Both conditions are true")

# Using 'or' operator
if x < 0 or y > 20:
    print("At least one condition is true")

# Using 'not' operator
if not(x == 0):
    print("x is not equal to 0")


# Prompt the user to enter Math score
math_score = int(input("Enter your Math score: "))

# Prompt the user to enter Science score
science_score = int(input("Enter your Science score: "))

# Check eligibility for the final exam
if math_score >= 60 and science_score >= 60:
    print("Congratulations! You are eligible to take the final exam.")
elif math_score >= 60 or science_score >= 60:
    print("You are eligible to retake the exam for the subject you scored below 60.")
else:
    print("Sorry, you are not eligible to take the final exam.")





# Ask the user for their age
age = int(input("Enter your age: "))

# Check if the age is greater than or equal to 18
if age >= 18:
    print("You age is suitable for voting.")
    
    # Nested condition to check if the user is a citizen
    citizenship = input("Are you a citizen? (yes/no): ")
    
    if citizenship.lower() == "yes":
        print("You can vote.")
    else:
        print("You must be a citizen to vote.")
else:
    print("You can't vote.")





# Ask the user if they are hungry
hungry = input("Are you hungry? (yes/no): ")

# Nested conditions based on user's hunger level
if hungry.lower() == "yes":
    # Ask the user to choose between pizza and pasta
    choice = input("Great! Would you like pizza or pasta? (pizza/pasta): ")
    
    if choice.lower() == "pizza":
        # Offer pizza toppings
        toppings = input("Would you like any toppings on your pizza? (yes/no): ")
        if toppings.lower() == "yes":
            print("Enjoy your customized pizza with your favorite toppings!")
        else:
            print("Enjoy your classic pizza!")
    
    elif choice.lower() == "pasta":
        # Offer pasta sauce options
        sauce = input("Would you like red sauce or white sauce on your pasta? (red/white): ")
        if sauce.lower() == "red":
            print("Enjoy your pasta with delicious marinara sauce!")
        elif sauce.lower() == "white":
            print("Enjoy your pasta with creamy Alfredo sauce!")
        else:
            print("Invalid sauce selection. Please choose between red and white sauce.")
    
    else:
        print("Invalid choice. Please choose between pizza and pasta.")
        
elif hungry.lower() == "no":
    print("No worries! Come back when you're hungry.")

else:
    print("Invalid response. Please enter 'yes' or 'no'.")
