import json
import os

# File used to store tasks
task_file = "my_tasks.json"

# Loading existing tasks or creating empty list
if os.path.exists(task_file):
    with open(task_file, "r") as f:
        task_list = json.load(f)
else:
    task_list = []

# Saving tasks to the file
def save_task_list():
    with open(task_file, "w") as f:
        json.dump(task_list, f, indent=2)

# To add a new task
def add_new_task():
    task_name = input("Type your new task: ")
    task_list.append({"task": task_name, "done": False})
    save_task_list()
    print(f"Task '{task_name}' added successfully!")

# To show all tasks that are added
def show_tasks():
    if not task_list:
        print("You have no tasks yet.")
        return
    for idx, task in enumerate(task_list, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{idx}. {task['task']} [{status}]")

# To mark a task as completed
def complete_task():
    show_tasks()
    try:
        num = int(input("Enter the number of the task to complete: "))
        if 1 <= num <= len(task_list):
            task_list[num-1]["done"] = True
            save_task_list()
            print("Task marked as done!")
        else:
            print("That task number does not exist.")
    except ValueError:
        print("Please enter a valid number.")

# To remove a task from the list
def remove_task():
    show_tasks()
    try:
        num = int(input("Enter the number of the task to delete: "))
        if 1 <= num <= len(task_list):
            removed_task = task_list.pop(num-1)
            save_task_list()
            print(f"Removed task: {removed_task['task']}")
        else:
            print("That task number does not exist.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
while True:
    print("\n--- My To-Do List ---")
    print("1. Add a task")
    print("2. Show tasks")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_new_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        print("Goodbye! Keep your tasks organized!")
        break
    else:
        print("Invalid option, try again.")
