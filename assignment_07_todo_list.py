def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print(f'Task added: "{task}"')


def view_tasks(tasks):
    if not tasks:
        print("Your task list is empty.")
        return

    print("Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def delete_task(tasks):
    if not tasks:
        print("Your task list is empty.")
        return

    view_tasks(tasks)
    choice = input("Enter task number to delete: ")

    if not choice.isdigit():
        print("Error: Invalid task number.")
        return

    index = int(choice)

    if index < 1 or index > len(tasks):
        print("Error: Invalid task number.")
        return

    removed_task = tasks.pop(index - 1)
    print(f'Task "{removed_task}" has been removed.')


def print_menu():
    print("============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def main():
    tasks = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")

        print()


if __name__ == "__main__":
    main()