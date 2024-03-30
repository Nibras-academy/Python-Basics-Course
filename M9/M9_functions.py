def bake_cookies():
    print("Mixing the ingredients...")
    print("Shaping the dough into cookies...")
    print("Baking the cookies in the oven...")
    print("Voila! Freshly baked cookies ready to delight your taste buds!")

# Call the function to bake cookies
bake_cookies()

def greet():
    print('Hello World!')
    
greet()


def calculate_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print("The area of the rectangle is:", area)

# Call the function to calculate and display the area
calculate_area()



def get_greeting():
    return "Hello, World!"

# Call the function and store the returned value in a variable
greeting_message = get_greeting()

print(greeting_message)  # Output: Hello, World!


# Function to input grades for each subject
def calc_grades():
    math_grade = float(input("Enter Math grade: "))
    english_grade = float(input("Enter English grade: "))
    science_grade = float(input("Enter Science grade: "))
    total_grades = math_grade + english_grade + science_grade
    average_grade = total_grades / 3
    return average_grade



average = calc_grades()
print("Average grade:", average)




# Function to display the menu options
def display_menu():
    print("Simple Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

# Function to perform addition
def add():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print("Result:", result)

# Function to perform subtraction
def subtract():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print("Result:", result)

# Function to perform multiplication
def multiply():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print("Result:", result)

# Function to perform division
def divide():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero!")


while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        add()
    elif choice == '2':
        subtract()
    elif choice == '3':
        multiply()
    elif choice == '4':
        divide()
    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
