# Task Management System using Python & Flask

## Project Overview

This is a Task Management System built with Python and Flask. It allows users to **add, view, update, and delete tasks** with a clean and responsive interface. Tasks are stored in a JSON file for simplicity.

---

## Features

* **Add Task:** Create a new task with title and description.
* **View Tasks:** See all tasks or filter by status (Pending/Completed).
* **Update Task:** Edit task details either by clicking 'Edit' or entering the Task ID.
* **Delete Task:** Remove a task safely with confirmation. Displays error if task not found.
* **Dashboard:** Shows total, pending, and completed tasks.
* **Toast Notifications:** Alerts for successful or failed operations.
* **Responsive Design:** Works on desktop and mobile screens.

---

## Technologies Used

* **Backend:** Python 3, Flask
* **Frontend:** HTML, CSS
* **Data Storage:** JSON file (`tasks.json`)
* **Hosting:** Vercel / GitHub Pages (optional)

---

## Folder Structure

```
GetZygo/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   ├── edit_task.html
│   ├── delete_task.html
│   ├── update_task.html
│   └── tasks.html
│
├── static/
│   └── style.css
│
├── tasks.json
├── app.py
├── requirements.txt
└── README.md
```

---

## Usage

1. Navigate to the dashboard to see task statistics.
2. Click **Add Task** to create a new task.
3. Click **Edit** or use **Update Task page** to modify tasks.
4. Use **Delete Task page** or buttons to remove tasks.
5. Filter tasks by **All, Pending, or Completed** in the dashboard.

---

## Future Enhancements

* Add user authentication and multiple user support.
* Use a database like SQLite or MySQL instead of JSON.
* Add due dates, priorities, and notifications.
* Mobile-friendly enhancements using frameworks like Bootstrap or Tailwind.

---

## License

This project is **open-source** and free to use.

---

## Author

**Mohammed Askee**
**askeeofficial2001@gmail.com**
