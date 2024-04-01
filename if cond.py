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





