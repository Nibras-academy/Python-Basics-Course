# Prompt the user to enter the price and quantity of each item
price_item1 = float(input("Enter the price of item 1: $"))
quantity_item1 = int(input("Enter the quantity of item 1: "))
price_item2 = float(input("Enter the price of item 2: $"))
quantity_item2 = int(input("Enter the quantity of item 2: "))

# Calculate the total cost for each item
total_cost_item1 = price_item1 * quantity_item1
total_cost_item2 = price_item2 * quantity_item2

# Calculate the total cost of all items
total_cost = total_cost_item1 + total_cost_item2

# Display the total cost of all items
print("The total cost of purchasing these items is: {}".format(total_cost))




# Define two strings
str1 = "Hello, "
str2 = "world!"

# Concatenate the strings
result = str1 + str2

# Display the result
print(result)  # Output: Hello, world!


import random


import random

# Generate a random floating-point number between 0 and 1
random_float = random.uniform(0, 1)
print("Random float:", random_float)



import random

# Generate a random integer between 1 and 10
random_number = random.randint(1, 10)
print("Random number:", random_number)



# Define the prices of the fruits
apple_price = 1.00
banana_price = 0.50
orange_price = 0.75

# Prompt the user to enter the quantity of each fruit
apple_quantity = int(input("Enter the quantity of apples you want to buy: "))
banana_quantity = int(input("Enter the quantity of bananas you want to buy: "))
orange_quantity = int(input("Enter the quantity of oranges you want to buy: "))

# Calculate the total cost of each fruit
total_apple_cost = apple_quantity * apple_price
total_banana_cost = banana_quantity * banana_price
total_orange_cost = orange_quantity * orange_price

# Calculate the overall total cost
total_cost = total_apple_cost + total_banana_cost + total_orange_cost

# Display the total cost to the user
print("Total cost of buying {} apples: ${:.2f}".format(apple_quantity, total_apple_cost))
print("Total cost of buying {} bananas: ${:.2f}".format(banana_quantity, total_banana_cost))
print("Total cost of buying {} oranges: ${:.2f}".format(orange_quantity, total_orange_cost))
print("Overall total cost: ${:.2f}".format(total_cost))




# Define the fixed prices of the fruits
apple_price = 1.00
banana_price = 0.50
orange_price = 0.75

# Generate random prices for each fruit - Repalce the above one with this
apple_price = random.randint(50, 150) / 100  # Random price between 0.50 and 1.50
banana_price = random.randint(25, 75) / 100  # Random price between 0.25 and 0.75
orange_price = random.randint(50, 100) / 100  # Random price between 0.50 and 1.00

# Define the fixed prices of the fruits
apple_price = 1.00
banana_price = 0.50
orange_price = 0.75

# Generate random prices for each fruit - Repalce the above one with this
apple_price = random.randint(50, 150) / 100  # Random price between 0.50 and 1.50
banana_price = random.randint(25, 75) / 100  # Random price between 0.25 and 0.75
orange_price = random.randint(50, 100) / 100  # Random price between 0.50 and 1.00
