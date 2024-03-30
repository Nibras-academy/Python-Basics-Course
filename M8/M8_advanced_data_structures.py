# Creating a tuple
my_tuple = (1, 2, 'hello', 3.5)

# Accessing elements
print(my_tuple[0])  # Output: 1

# Concatenation
new_tuple = my_tuple + (4, 5)
print(new_tuple)   # Output: (1, 2, 'hello', 3.5, 4, 5)

# Repetition
repeated_tuple = my_tuple * 2
print(repeated_tuple)  # Output: (1, 2, 'hello', 3.5, 1, 2, 'hello', 3.5)

# Length
print(len(my_tuple))   # Output: 4

# Membership
print('hello' in my_tuple)  # Output: True




# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)
print(my_set)   # Output: {1, 2, 3, 4, 5, 6}

# Removing elements
my_set.remove(3)
print(my_set)   # Output: {1, 2, 4, 5, 6}

# Union
other_set = {4, 5, 6, 7, 8}
union_set = my_set.union(other_set)
print(union_set)    # Output: {1, 2, 4, 5, 6, 7, 8}

# Intersection
intersection_set = my_set.intersection(other_set)
print(intersection_set)   # Output: {4, 5, 6}

# Difference
difference_set = my_set.difference(other_set)
print(difference_set)   # Output: {1, 2}

print(len(my_set))   # Output: 5



animal_dict = {
    'lion': 'The king of the jungle with a magnificent mane.',
    'elephant': 'A gentle giant with a long trunk and big ears.',
    'giraffe': 'A tall animal with a long neck and a spotted coat.',
    'penguin': 'A cute bird that waddles and swims in icy waters.'
}




print(animal_dict['lion'])  # Output: The king of the jungle with a magnificent mane.


animal_dict['tiger'] = 'A majestic big cat with orange fur and black stripes.'
animal_dict['lion'] = 'The king of the jungle with a majestic mane.'
print(animal_dict)


del animal_dict['giraffe']
description = animal_dict.pop('elephant')
print(animal_dict)

print(len(animal_dict))  # Output: 3


print('lion' in animal_dict)  # Output: True


print(animal_dict.keys())  # Output: dict_keys(['lion', 'tiger', 'penguin'])


print(animal_dict.values())  # Output: dict_values(['The king of the jungle with a majestic mane.', 'A majestic big cat with orange fur and black stripes.', 'A cute bird that waddles and swims in icy waters.'])



# -------------------------------- School System--------------------------------------------------#

# Initialize an empty dictionary to store student records
student_records = []

# Main menu options
menu = """
Student Management System
1. Add Student
2. Update Student
3. Delete Student
4. View All Students
5. Exit
"""

# Main loop to display the menu and handle user input
while True:
    print(menu)
    choice = input("Enter your choice: ")

    # Add Student
    if choice == '1':
        student = {}
        student['id'] = input("Enter student ID: ")
        student['name'] = input("Enter student name: ")
        student['department'] = input("Enter student department: ")
        student_records.append(student)
        print("Student added successfully!")

    # Update Student
    elif choice == '2':
        id_to_update = input("Enter the ID of the student to update: ")
        for student in student_records:
            if student['id'] == id_to_update:
                student['name'] = input("Enter updated name: ")
                student['department'] = input("Enter updated department: ")
                print("Student updated successfully!")
                break
        else:
            print("Student not found!")

    # Delete Student
    elif choice == '3':
        id_to_delete = input("Enter the ID of the student to delete: ")
        for student in student_records:
            if student['id'] == id_to_delete:
                student_records.remove(student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found!")

    # View All Students
    elif choice == '4':
        if not student_records:
            print("No students found!")
        else:
            print("ID -  Name  -  Department")
            for student in student_records:
                print(student['id'],' - ',student['name'], ' - ', student['department'])

    # Exit
    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")



students = [
    {"id": 101, "name": "Ahmed", "grade": "A"},
    {"id": 102, "name": "Khaled", "grade": "B"},
    {"id": 103, "name": "Aly", "grade": "C"}
]