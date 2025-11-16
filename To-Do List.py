import os

TODO_FILE = "todo.txt"

def show_menu():
    print("
==== To-Do List Menu ====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def read_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def write_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "
")

def view_tasks():
    tasks = read_tasks()
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("Your tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter the task to add: ")
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)
    print("Task added successfully.")

def remove_task():
    tasks = read_tasks()
    if not tasks:
        print("No tasks to remove.")
        return
    view_tasks()
    idx = int(input("Enter task number to remove: ")) - 1
    if 0 <= idx < len(tasks):
        removed = tasks.pop(idx)
        write_tasks(tasks)
        print(f"Task '{removed}' removed.")
    else:
        print("Invalid task number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()