import json
import os

# Initialize JSON file if not exists
if not os.path.exists("data.json"):
    with open("data.json", "w") as f:
        json.dump({}, f)


def load_data():
    with open("data.json", "r") as f:
        return json.load(f)


def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


def signup():
    data = load_data()
    username = input("Enter a username: ")
    if username in data:
        print(" Username already exists.")
        return

    password = input("Enter a password: ")
    data[username] = {"password": password, "tasks": []}
    save_data(data)
    print(" Signup successful!")


def login():
    data = load_data()
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in data and data[username]["password"] == password:
        print("✅ Login successful!")
        return username
    else:
        print(" Invalid credentials.")
        return None


def add_task(username):
    data = load_data()
    task = input("Enter your task: ")
    data[username]["tasks"].append(task)
    save_data(data)
    print(" Task added!")


def view_tasks(username):
    data = load_data()
    tasks = data[username]["tasks"]
    if not tasks:
        print("📭 No tasks yet.")
    else:
        print(" Your Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")


def edit_task(username):
    data = load_data()
    tasks = data[username]["tasks"]
    view_tasks(username)
    if not tasks:
        return
    try:
        choice = int(input("Enter task number to edit: ")) - 1
        if 0 <= choice < len(tasks):
            new_task = input("Enter new task: ")
            tasks[choice] = new_task
            save_data(data)
            print("Task updated!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(username):
    data = load_data()
    tasks = data[username]["tasks"]
    view_tasks(username)
    if not tasks:
        return
    try:
        choice = int(input("Enter task number to delete: ")) - 1
        if 0 <= choice < len(tasks):
            tasks.pop(choice)
            save_data(data)
            print("Task deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# ==========================
# MAIN PROGRAM
# ==========================
print("--------- Daily Task Tracker ---------")

while True:
    action = input("\n1 - Signup\n2 - Login\n3 - Exit\nChoose: ")

    if action == "1":
        signup()
    elif action == "2":
        user = login()
        if user:
            while True:
                print(f"\nWelcome, {user}")
                choice = input(
                    "1 - View Tasks\n2 - Add Task\n3 - Edit Task\n4 - Delete Task\n5 - Logout\nChoose: "
                )
                if choice == "1":
                    view_tasks(user)
                elif choice == "2":
                    add_task(user)
                elif choice == "3":
                    edit_task(user)
                elif choice == "4":
                    delete_task(user)
                elif choice == "5":
                    print("👋 Logged out.")
                    break
                else:
                    print("Invalid option.")
    elif action == "3":
        print("👋 Goodbye!")
        break
    else:
        print("Please enter 1, 2, or 3.")
