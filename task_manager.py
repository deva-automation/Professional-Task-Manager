import json
import os

# Database file name
FILE_NAME = "tasks.json"

def load_tasks():
    """Function to load data from JSON file"""
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """Function to save data to JSON file"""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """Function to add a new task"""
    task_name = input("📝 Enter the new task: ")
    tasks.append({"task": task_name, "status": "Pending"})
    save_tasks(tasks)
    print(f"✅ Task '{task_name}' added successfully!")

def view_tasks(tasks):
    """Function to display all tasks"""
    if not tasks:
        print("📭 No tasks found! Your list is empty.")
        return
    
    print("\n📋 --- Your Task List ---")
    for index, item in enumerate(tasks, start=1):
        print(f"[{index}] {item['task']} - ({item['status']})")
    print("------------------------\n")

def delete_task(tasks):
    """Function to delete a task by index"""
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("🗑️ Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"✅ Task '{removed['task']}' deleted!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    """Main menu loop"""
    tasks = load_tasks()
    
    while True:
        print("\n⚙️  MAIN MENU")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("👉 Choose an option (1/2/3/4): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("👋 Exiting program. Have a productive day!")
            break
        else:
            print("❌ Invalid choice! Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
    