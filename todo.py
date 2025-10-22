# todo.py
# Simple Console-based To-Do List Application
# Author: Sachin Meethal

TASKS_FILE = "tasks.txt"

# Function to load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to display tasks
def view_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks found!\n")
    else:
        print("\n Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print()

# Function to add a new task
def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"✅ Task '{task}' added successfully!\n")
    else:
        print("⚠️ Task cannot be empty.\n")

# Function to remove a task
def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed_task}' removed successfully!\n")
        else:
            print("⚠️ Invalid task number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

# Main program loop
def main():
    tasks = load_tasks()
    while True:
        print("====== TO-DO LIST MENU ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1–4.\n")

if __name__ == "__main__":
    main()
