# Start by asking the user if they are hungry
hungry = input("Are you hungry? (yes/no): ")

# Check if the user is hungry
if hungry.lower() == 'yes':
    # If the user is hungry, ask what meal they want
    meal_choice = input("Do you want pizza or pasta? ").lower()
    
    # Check the meal choice
    if meal_choice == 'pizza':
        # If the user wants pizza, ask for pizza preferences
        pizza_toppings = input("Do you want pepperoni on your pizza? (yes/no): ").lower()
        if pizza_toppings == 'yes':
            print("You're hungry and you want pizza with pepperoni.")
        else:
            print("You're hungry and you want pizza without pepperoni.")
    elif meal_choice == 'pasta':
        # If the user wants pasta, ask for pasta preferences
        pasta_sauce = input("Do you want marinara sauce on your pasta? (yes/no): ").lower()
        if pasta_sauce == 'yes':
            print("You're hungry and you want pasta with marinara sauce.")
        else:
            print("You're hungry and you want pasta without marinara sauce.")
    else:
        print("Invalid choice. Please choose between pizza and pasta.")
elif hungry.lower() == 'no':
    # If the user is not hungry, display a message
    print("That's okay. Have a good day!")
else:
    # If the user inputs an invalid response, display an error message
    print("Invalid input. Please enter 'yes' or 'no'.")
