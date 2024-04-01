# Print the multiplication table of a given number using a for loop
num = int(input("Enter a number: "))
print("Multiplication Table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
