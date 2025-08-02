
markdown
Copy
Edit
# 🗂️ Task Tracker - Python CLI App

A simple **command-line** task tracker app built in **Python** that allows users to **sign up**, **log in**, and **manage their daily tasks**. All user data and tasks are saved in a single `task_data.json` file using JSON.

---

## ✅ Features

- 🔐 User Signup & Login (username + password)
- 📝 Create, View, Edit, and Delete personal tasks
- 💾 All data saved persistently in `task_data.json`
- 📦 Multi-user support
- 🧠 Simple logic with beginner-friendly code

---

## 📂 File Structure

task_tracker/
│
├── task_tracker.py # Main application file
├── task_data.json # Stores all user accounts and tasks
└── README.md # Project description and instructions

yaml
Copy
Edit

---

## 🚀 How to Run

1. **Clone or download the project**  
git clone https://github.com/yourusername/task-tracker-python.git

markdown
Copy
Edit

2. **Navigate to the project folder**
cd task-tracker-python

markdown
Copy
Edit

3. **Run the script**
python task_tracker.py

yaml
Copy
Edit

> Make sure you have Python installed (version 3.6 or higher).

---

## 💡 How It Works

1. User chooses **Signup** or **Login**.
2. After logging in:
- View all your tasks
- Add a new task
- Edit an existing task
- Delete a task
- Logout to return to the main menu
3. All user data and tasks are stored in `task_data.json` like this:

```json
{
"suleman": {
 "password": "1234",
 "tasks": [
   "Finish homework",
   "Workout at 6 PM"
 ]
}
}
📘 JSON Functions Used
json.load() → Reads data from JSON file into Python dictionary

json.dump() → Saves Python dictionary back into JSON file

These ensure data is kept even after program ends.

🎯 Future Improvements
✅ Mark tasks as completed/incomplete

📅 Add task deadlines

🔍 Search/filter tasks

🖥️ GUI using Tkinter or Flask

🧠 Why This Project?
This project is perfect for Python beginners to practice:

File handling

User input

JSON storage

Loop and function logic

Basic user authentication

🛠️ Requirements
Python 3.6+

No external libraries needed

📄 License
This project is licensed under the MIT License.

👤 Author
Suleman Gulzar
Learning Python and building useful tools one step at a time!
