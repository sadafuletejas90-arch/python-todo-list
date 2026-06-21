# =====================================
# Project Name: To-Do List
# Author: Tejas Sadafule
# Language: Python
# Description: A simple task management application
# Version: 1.0
# =====================================

# Create an empty list to store tasks
tasks = []

# Run the program continuously
while True:

    # Display menu options
    print("\n===== TODO LIST ===== - python-to-do-list.py:16")
    print("1. Add Task - python-to-do-list.py:17")
    print("2. View Tasks - python-to-do-list.py:18")
    print("3. Remove Task - python-to-do-list.py:19")
    print("4. Exit - python-to-do-list.py:20")

    # Ask user for choice
    choice = input("Enter your choice: ")

    # Add a new task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully! - python-to-do-list.py:29")

    # Display all tasks
    elif choice == "2":

        # Check if task list is empty
        if len(tasks) == 0:
            print("No tasks available. - python-to-do-list.py:36")

        else:
            print("\nYour Tasks: - python-to-do-list.py:39")

            # Display all tasks with numbers
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task} - python-to-do-list.py:43")

    # Remove a task
    elif choice == "3":

        # Check if list is empty
        if len(tasks) == 0:
            print("No tasks to remove. - python-to-do-list.py:50")

        else:
            # Show tasks
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task} - python-to-do-list.py:55")

            task_num = int(input("Enter task number to remove: "))

            # Validate task number
            if 1 <= task_num <= len(tasks):

                # Remove selected task
                removed = tasks.pop(task_num - 1)

                print(f"Removed: {removed} - python-to-do-list.py:65")

            else:
                print("Invalid task number. - python-to-do-list.py:68")

    # Exit the application
    elif choice == "4":
        print("Goodbye! - python-to-do-list.py:72")
        break

    # Handle invalid choices
    else:
        print("Invalid choice. Try again. - python-to-do-list.py:77")