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
