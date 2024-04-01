# Step 1: Ask the user to input the total number of students attending the event
total_students = int(input("Enter the total number of students attending the event: "))

# Step 2: Calculate the number of full rows
full_rows = total_students // 8

# Step 3: Calculate the number of students left over
students_leftover = total_students % 8

# Step 4: Print the results
print("Number of full rows:", full_rows)
print("Number of students left over:", students_leftover)

