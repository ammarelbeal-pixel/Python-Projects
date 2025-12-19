# Student Management System
# Simple Python Project for Beginners

students = []  # list to store students


def add_student():          #function to add a student
    name = input("Enter student name: ")
    grade = float(input("Enter student grade (0 - 100): ")) #why float? _because the degree could be a fraction.
    students.append([name, grade])      #.append? _to add an item at the end of the list.
    print("Student added successfully!\n")      # \n?   _To move to the next line


def show_students():            
    if not students:
        print("No students found.\n")
        return

    print("\nStudents List:")
    for i, student in enumerate(students, start=1): # enumerate gives you the student's number and details.
        print(f"{i}. Name: {student[0]} | Grade: {student[1]}")
    print()


def calculate_average():
    if not students:
        print("No students to calculate average.\n")
        return

    total = 0       # variable to collect the degrees.
    for student in students:
        total += student[1]

    average = total / len(students)     # len(students)?  _To calculate the number of items in the list. 
    print(f"Average grade = {average:.2f}\n")


def save_to_file():     # save data in a file.
    with open("students.txt", "w") as file: # open a file to writing.
        for student in students:
            file.write(f"{student[0]} - {student[1]}\n")
    print("Data saved to students.txt\n")


while True:     # infinite loop
    print("===== Student Management System =====")
    print("1. Add student")
    print("2. Show students")
    print("3. Calculate average")
    print("4. Save to file")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        calculate_average()
    elif choice == "4":
        save_to_file()
    elif choice == "5":
        print("Thank you ,Have a nice day !")
        break
    else:
        print("Invalid choice, try again.\n")
