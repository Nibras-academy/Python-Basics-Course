
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
print("Total cost of buying", apple_quantity, "apples: $", total_apple_cost)
print("Total cost of buying", banana_quantity, "bananas: $", total_banana_cost)
print("Total cost of buying", orange_quantity, "oranges: $", total_orange_cost)
print("Overall total cost: $", total_cost)

