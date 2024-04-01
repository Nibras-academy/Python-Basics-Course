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

