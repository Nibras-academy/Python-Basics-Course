

















# Example:
x = 10
name = "John"

# Assign new variable using another variable
new_name = name

# changing the value of your variables
new_name = "Sam"

# Outputting
print(new_name)


# Addition
result = 10 + 5

# Subtraction
result = 20 - 8

# Multiplication
result = 3 * 4

# Division
result = 15 / 3

# Modulus (remainder)
result = 10 % 3

# Exponentiation
result = 2 ** 3

# Example:
result = 10 % 3
print(result)  # Output: 1



# Equal to
print(10 == 5)  # Output: False

# Not equal to
print(20 != 8)  # Output: True

# Greater than
print(15 > 3)   # Output: True

# Less than
print(10 < 3)   # Output: False

# Greater than or equal to
print(8 >= 8)   # Output: True

# Less than or equal to
print(10 <= 3)  # Output: False


# Define the prices of the fruits
apple_price = 1.00
banana_price = 0.50
orange_price = 0.75

# Prompt the user to enter the quantity of each fruit
apple_quantity = int(input("Enter the quantity of apples: "))
banana_quantity = int(input("Enter the quantity of bananas: "))
orange_quantity = int(input("Enter the quantity of oranges: "))

# Calculate the total cost of each fruit
total_apple_cost = apple_quantity * apple_price
total_banana_cost = banana_quantity * banana_price
total_orange_cost = orange_quantity * orange_price

# Calculate the overall total cost
total_cost = total_apple_cost + total_banana_cost + total_orange_cost

# Display the total cost to the user with commas for readability
print(f"Total cost of buying {apple_quantity:,} apples: ${total_apple_cost:,.2f}")
print(f"Total cost of buying {banana_quantity:,} bananas: ${total_banana_cost:,.2f}")
print(f"Total cost of buying {orange_quantity:,} oranges: ${total_orange_cost:,.2f}")
print(f"Overall total cost: ${total_cost:,.2f}")
