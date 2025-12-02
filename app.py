# app.py - Final Professional Task Manager with Direct Edit
from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = "secret123"
TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def get_next_id():
    tasks = load_tasks()
    return max([t.get("task_id", 0) for t in tasks] + [0]) + 1

# ==================== ROUTES ====================
@app.route("/")
def dashboard():
    tasks = load_tasks()
    status = request.args.get("status")
    if status in ["Pending", "Completed"]:
        tasks = [t for t in tasks if t["status"] == status]

    total = len(load_tasks())
    pending = len([t for t in load_tasks() if t["status"] == "Pending"])
    completed = total - pending

    return render_template("index.html", tasks=tasks, total=total, pending=pending, completed=completed)

@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        title = request.form["title"].strip()
        desc = request.form["description"].strip()
        if not title:
            flash("Title is required!", "error")
            return render_template("add.html")

        tasks = load_tasks()
        tasks.append({
            "task_id": get_next_id(),
            "title": title,
            "description": desc or "No description",
            "status": "Pending"
        })
        save_tasks(tasks)
        flash("Task added successfully!", "success")
        return redirect(url_for("dashboard"))
    return render_template("add.html")

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    tasks = load_tasks()
    task = next((t for t in tasks if t["task_id"] == task_id), None)

    if not task:
        flash("Task not found!", "error")
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        title = request.form["title"].strip()
        desc = request.form["description"].strip()
        if not title:
            flash("Title cannot be empty!", "error")
        else:
            task["title"] = title
            task["description"] = desc or "No description"
            if "complete" in request.form:
                task["status"] = "Completed"
            save_tasks(tasks)
            flash("Task updated successfully!", "success")
        return redirect(url_for("dashboard"))

    return render_template("edit_task.html", task=task)

# ==================== NEW FEATURE: Update Task Page ====================
@app.route("/update", methods=["GET", "POST"])
def update_task_form():
    if request.method == "POST":
        try:
            task_id = int(request.form["task_id"])
        except:
            flash("Invalid Task ID!", "error")
            return redirect(url_for("update_task_form"))

        tasks = load_tasks()
        task = next((t for t in tasks if t["task_id"] == task_id), None)

        if task:
            return redirect(url_for("edit_task", task_id=task_id))
        else:
            flash("Task not found!", "error")
            return redirect(url_for("update_task_form"))

    return render_template("update_task.html")

# ==================== NEW FEATURE: Delete Task Page ====================
@app.route("/delete-task", methods=["GET", "POST"])
def delete_task_form():
    if request.method == "POST":
        try:
            task_id = int(request.form["task_id"])
        except:
            flash("Invalid Task ID!", "error")
            return redirect(url_for("delete_task_form"))

        tasks = load_tasks()
        task = next((t for t in tasks if t["task_id"] == task_id), None)

        if task:
            tasks = [t for t in tasks if t["task_id"] != task_id]
            save_tasks(tasks)
            flash("Task deleted successfully!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Task not found!", "error")
            return redirect(url_for("delete_task_form"))

    return render_template("delete_task.html")

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["task_id"] != task_id]
    save_tasks(tasks)
    flash("Task deleted!", "success")
    return redirect(url_for("dashboard"))

@app.route("/tasks")
def view_tasks():
    return render_template("tasks.html", tasks=load_tasks())

if __name__ == "__main__":
    app.run() # For Production purpose
