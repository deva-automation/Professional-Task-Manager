import json
import os

# ডাটাবেস ফাইলের নাম
FILE_NAME = "tasks.json"

def load_tasks():
    """JSON ফাইল থেকে ডাটা লোড করার ফাংশন"""
    # যদি ফাইল না থাকে, তবে একটি ফাঁকা লিস্ট রিটার্ন করবে
    if not os.path.exists(FILE_NAME):
        return []
    
    # ফাইল থাকলে ডাটা রিড করবে
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """নতুন ডাটা JSON ফাইলে সেভ করার ফাংশন"""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """নতুন কাজ যুক্ত করার ফাংশন"""
    task_name = input("📝 Enter the new task: ")
    tasks.append({"task": task_name, "status": "Pending"})
    save_tasks(tasks)
    print(f"✅ Task '{task_name}' added successfully!")

def view_tasks(tasks):
    """সব কাজ দেখার ফাংশন"""
    if not tasks:
        print("📭 No tasks found! Your list is empty.")
        return
    
    print("\n📋 --- Your Task List ---")
    for index, item in enumerate(tasks, start=1):
        print(f"[{index}] {item['task']} - ({item['status']})")
    print("------------------------\n")

def delete_task(tasks):
    """কাজ ডিলিট করার ফাংশন"""
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
    """মেইন মেনু লুপ (প্রোগ্রাম এখান থেকে শুরু হবে)"""
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
    