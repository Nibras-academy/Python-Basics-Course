########## Restaurant ###########

def display_menu(menu):
    print("Welcome to our restaurant! Here's our menu:\n")
    for item, price in menu.items():
        print(f"{item}: ${price}")

def take_orders(menu):
    order = {}
    print("\nPlease enter the number of each item you'd like to order:")
    for item in menu:
        quantity = int(input(f"{item}: "))
        order[item] = quantity
    return order

def calculate_total(menu, order):
    total_price = 0  # Initialize total price to zero
    for item, quantity in order.items():  # Iterate over items in the order
        total_price += menu[item] * quantity  # Add price of each item to total
    return total_price  # Return the total price

menu = {
    'Burger': 10,
    'Pizza': 12,
    'Salad': 8,
    'Fries': 4
}

print("Welcome to our restaurant! Here's our menu:\n")
display_menu(menu)

while True:
    order = take_orders(menu)
    total_price = calculate_total(menu, order)
    print(f"\nThank you for your order! Your total is: ${total_price}")

    choice = input("\nWould you like to place another order? (yes/no): ")
    if choice.lower() != 'yes':
        break