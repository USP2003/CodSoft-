# A To-Do List application is a useful project that helps users manage and organize their tasks efficiently. This project aims to create a command-line or GUI-based application using Python, allowing users to create, update, and track their to-do lists

# Simple To-Do List in Python

tasks = []

def show_menu():
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

def add_task():
    task = input("\nEnter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    print("\n===== Your To-Do List =====")
    for i, task in enumerate(tasks, 1):
        status = " [X]" if task["completed"] else " [ ]"
        print(f"{i}. {task['task']}{status}")

def mark_completed():
    view_tasks()
    task_number = int(input("\nEnter the task number to mark as completed (0 to cancel): "))
    
    if task_number == 0 or task_number > len(tasks):
        print("Invalid task number. Task not marked as completed.")
    else:
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed!")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
