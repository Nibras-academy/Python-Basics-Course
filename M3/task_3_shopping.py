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
print("The total cost: {}".format(total_cost))