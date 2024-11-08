# ------------------------------------------------------------------------------------------ #
# Title: Working with conditions and loops
# Desc: Shows how conditional logic statements work
# Change Log: (Who, When, What)
# RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the program's data

## Constants
FILE_NAME: str = "A05/Enrollments.csv"
MENU: str = '''
--- Course Registration Program ---
 Select from the following menu:
 1. Register a Student for a Course
 2. Show current data
 3. Save data to a file
 4. Exit the program
 ----------------------------------
'''

## Variable Declaration and Initialization
student_first_name: str = str()
student_last_name: str = str()
course_name: str = str()
csv_data: str = str()
file_obj = None
menu_choice: str = str()
student_data: list = [] # Holds information about 1 student.
students: list[list[str]] = [] # Holds list of list student information.

# init student data with data from Enrollements file
with open(FILE_NAME, "r") as file_obj:
    for row in file_obj.readlines():
        # done if row is just a newline
        if (row == '\n'):
            break
        student_data = row.strip().split(',')
        students.append(student_data)

# Input the data
while menu_choice != '4':
    print(MENU)
    menu_choice = input('Enter 1-4 to select action: ')
    # Get input from the user before quitting the program
    if menu_choice == '1':
        # print(menu_choice)
        # Input
        while True:
            student_first_name = input("Student First Name: ")
            student_last_name = input("Student Last Name: ")
            course_name = input("Course Name: ")
            if (len(student_first_name) > 0 or len(student_last_name) > 0 or len(course_name) > 0):
                # csv data will contain data added during this session
                csv_data += f"{student_first_name},{student_last_name},{course_name}\n"
                # add input data to data from file
                student_data = [student_first_name,student_last_name,course_name]
                students.append(student_data)
                break
            else:
                print("incomplete data - you must enter data for all fields - try again ")

    # Output the data
    elif menu_choice == '2':
        # Output
        if (len(csv_data) == 0):
            print("no data added during this session")
        else:
            print(f'data from this session:\n{csv_data}')
        print('All data:')
        for student_data in students:
            # print(student_data)
            student_first_name,student_last_name,course_name = student_data
            print(f'{student_first_name},{student_last_name},{course_name}')
    # Process the data to create custom messages
    elif menu_choice == '3':
        file_obj = open(FILE_NAME, 'w')
        with open(FILE_NAME, "w") as file_obj:
            for student_data in students:
                student_first_name, student_last_name, course_name = student_data
                file_obj.write(f'{student_first_name},{student_last_name},{course_name}\n')
    elif menu_choice == '4':
        print("Program Ending")
        break
    else:
        print("\nYou entered an unrecognized option.")





