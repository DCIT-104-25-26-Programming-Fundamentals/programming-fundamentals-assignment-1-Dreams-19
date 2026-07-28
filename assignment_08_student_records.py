def calculate_average(scores):
    return round(sum(scores) / len(scores), 2)


def add_student(students):
    name = input("Student name: ")
    student_id = int(input("Student ID: "))
    num_scores = int(input("How many scores? "))

    scores = []
    for i in range(1, num_scores + 1):
        score = int(input(f"Enter score {i}: "))
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)

    print(f'Student "{name}" added successfully.')


def display_all_students(students):
    if not students:
        print("No students have been added yet.")
        return

    print("-" * 50)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average':<10}")
    print("-" * 50)

    for student in students:
        scores_str = ", ".join(str(score) for score in student["scores"])
        average = calculate_average(student["scores"])
        print(f"{student['name']:<15}{student['id']:<12}{scores_str:<15}{average:<10}")

    print("-" * 50)


def calculate_average_for_student(students):
    student_id = int(input("Enter student ID: "))

    for student in students:
        if student["id"] == student_id:
            average = calculate_average(student["scores"])
            print(f"{student['name']}'s average score: {average}")
            return

    print("Error: Student ID not found.")


def print_menu():
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    students = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            calculate_average_for_student(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")

        print()


if __name__ == "__main__":
    main()