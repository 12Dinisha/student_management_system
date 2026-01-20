students = []


def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course name: ")

    student = {
        "name": name,
        "roll": roll,
        "course": course
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- Student List ---")
    for student in students:
        print(
            f"Name: {student['name']}, "
            f"Roll No: {student['roll']}, "
            f"Course: {student['course']}"
        )


def search_student():
    roll = input("Enter roll number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found:")
            print(
                f"Name: {student['name']}, "
                f"Roll No: {student['roll']}, "
                f"Course: {student['course']}"
            )
            return

    print("Student not found.")


def delete_student():
    roll = input("Enter roll number to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def show_menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")


def main():
    print("Welcome to Student Management System")

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
