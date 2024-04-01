
# Task 4 - General Question
# Prompt the user to enter a temperature in Celsius
celsius_str = input("Enter the temperature in Celsius: ")

# Convert the Celsius temperature to a floating-point number
celsius = float(celsius_str)

# Convert Celsius to Fahrenheit using the formula
fahrenheit = (celsius * 9/5) + 32

# Display the converted temperature in Fahrenheit to the user
print("The temperature in Fahrenheit is:", round(fahrenheit, 2))
