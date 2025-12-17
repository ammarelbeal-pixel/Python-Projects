students = []     #list

n = int(input("Enter number of students: "))

if n <= 0:
    print("No students to enter!")   # to avoid any Error
else:
    for i in range(n):
        name = input("Enter student name: ")
        grade = float(input("Enter student grade (0-100): "))

        students.append([name, grade])      # (. append ) to add an element

    with open("grades.txt", "w") as file:           #open the file to write.
        for student in students:
            file.write(student[0] + " - " + str(student[1]) + "\n")

    print("\nStudents Grades:")
    for student in students:
        print(student[0], ":", student[1])

    grades = [student[1] for student in students]
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)

    print(f"\nAverage Grade: {average:.3f}")
    print(f"Highest Grade: {highest}for the student{highest}")
    print(f"Lowest Grade: {lowest}for the student{lowest}")









