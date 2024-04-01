car1_make = "Toyota"
car1_model = "Camry"
car1_color = "Red"
car1_price = 25000

decoration = "-" * 30
print(decoration)

car1_info = f"Car: {car1_make} {car1_model}, with color: {car1_color}, and the price is: ${car1_price}"
print(car1_info)
print(car1_info[:20])  # Display only the first 20 characters of the car information


print(f"Car: {car1_make} {car1_model}")

car1_color_upper = car1_color.upper()  # Convert color to uppercase

print(f"Color: {car1_color_upper}")
print(f"Price: {car1_price}")

car1_model_length = len(car1_model)
print(f"No. of letters in Model: {car1_model_length}")

car1_model_length = len(car1_model)

car1_info = "Car: " + car1_make + " " + car1_model + ", with color: " + car1_color + ", and the price is: $" + str(car1_price)
print(car1_info)

car1_make_lower = car1_make.lower()


car_data = "Toyota,Camry,Red,25000"
car_data_list = car_data.split(",")
print(car_data_list)
print(type(car_data_list))   # Output: <class 'list'>

# Lists for different categories of car details
car_makes = ["Toyota", "Honda", "Ford", "Chevrolet"]
car_models = ["Camry", "Accord", "F-150", "Silverado"]
car_colors = ["Red", "Blue", "Black", "White"]
car_prices = [25000, 28000, 30000, 32000]


print(car_makes[0])    # Output: "Toyota"

# Details of the first car
first_car_make = car_makes[0]
first_car_model = car_models[0]
first_car_color = car_colors[0]
first_car_price = car_prices[0]

# Print details of the first car
print("First Car Details:")
print("Make:", first_car_make)
print("Model:", first_car_model)
print("Color:", first_car_color)
print("Price: $", first_car_price)

# Modifying elements of car lists
car_makes[0] = "Nissan"
car_models[0] = "Sunny"
car_colors[1] = "Silver"
car_prices[2] += 1000

print("The lists before modification:")
print(car_makes)
print(car_models)

# Adding elements to car lists
car_makes.append("Subaru")
car_models.insert(2, "Civic")

print("The lists After modification:")
print(car_makes)
print(car_models)


print("The lists before modification:")
print(car_colors)
print(car_prices)

# Removing elements from car lists
car_colors.remove("Red")
del car_prices[1]

print("The lists After modification:")
print(car_colors)
print(car_prices)

# Ask the user to select a car model
selected_model = input("Enter the car model you want to see details for from: Sunny, Accord, F-150, Silverado: ")

# Find the index of the selected car model
index = car_models.index(selected_model)

# Retrieve the details of the selected car model
selected_make = car_makes[index]
selected_color = car_colors[index]
selected_price = car_prices[index]

# Display the details of the selected car model
print("Details for {}:".format(selected_model))
print("Make:", selected_make)
print("Color:", selected_color)
print("Price: ${}".format(selected_price))


 
 
 