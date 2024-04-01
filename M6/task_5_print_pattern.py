# Define the size of the square
size = 5

# Iterate over each row
for i in range(5):
    # For the first and last rows, or the first and last columns, print '*' for each column
    if i == 0 or i == 4:
        print('******')
    else:
        # For other rows, print '*' for the first and last columns, and spaces for the middle columns
        print('*    *')
        