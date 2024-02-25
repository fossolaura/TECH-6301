#Requirements

#Develop a simple task list manager that allows users to add, remove, 
#and view tasks. The program should save the task list to a text file 
#and handle exceptions in a controlled manner.

import json

# File path for storing tasks
tasks_file_path = 'tasks.json'

def add_task(tasks, task):
    """Add a new task to the list."""
    tasks.append(task)
    print(f"Task added: {task}")

def remove_completed_tasks(tasks):
    """Remove completed tasks from the list."""
    tasks[:] = [task for task in tasks if not task.get('completed', False)]
    print("Completed tasks removed.")

def view_tasks(tasks):
    """View the current task list."""
    if tasks:
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task.get('completed', False) else "Pending"
            print(f"{i}. {task['name']} - {status}")
    else:
        print("No tasks found.")

def save_tasks(tasks):
    """Save tasks to a file."""
    try:
        with open(tasks_file_path, 'w') as file:
            json.dump(tasks, file)
        print("Tasks saved successfully.")
    except Exception as e:
        print(f"Failed to save tasks: {e}")

def load_tasks():
    """Load tasks from a file."""
    try:
        with open(tasks_file_path, 'r') as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        print("No saved tasks found. Starting with an empty list.")
        return []
    except Exception as e:
        print(f"Failed to load tasks: {e}")
        return []

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTask List Manager")
        print("1. Add Task")
        print("2. Remove Completed Tasks")
        print("3. View Tasks")
        print("4. Save and Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            task_name = input("Enter task name: ")
            add_task(tasks, {'name': task_name, 'completed': False})
        elif choice == '2':
            remove_completed_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
