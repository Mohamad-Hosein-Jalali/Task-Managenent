import tkinter as tk
from tkinter import messagebox, simpledialog
import json

TASKS_FILE = "tasks.json"


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    title = simpledialog.askstring("Add Management", "Tittle:")
    if title:
        description = simpledialog.askstring("Add Management", "Description:")
        if description:
            tasks.append({"title": title, "description": description, "completed": False})
            save_tasks(tasks)
            update_task_list()


def update_task_list():
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✅" if task["completed"] else "❌"
        task_list.insert(tk.END, f"{status} {task['title']} - {task['description']}")


def complete_task():
    selected_index = task_list.curselection()
    if selected_index:
        index = selected_index[0]
        tasks[index]["completed"] = True
        save_tasks(tasks)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please select a management. ")


def delete_task():
    selected_index = task_list.curselection()
    if selected_index:
        index = selected_index[0]
        del tasks[index]
        save_tasks(tasks)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please select a management. ")


tasks = load_tasks()

root = tk.Tk()
root.title("Tasl Management")

task_list = tk.Listbox(root, width=50, height=15)
task_list.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

btn_add = tk.Button(btn_frame, text="Add", command=add_task)
btn_add.grid(row=0, column=0, padx=5)

btn_complete = tk.Button(btn_frame, text="Mark", command=complete_task)
btn_complete.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(btn_frame, text="Delete", command=delete_task)
btn_delete.grid(row=0, column=2, padx=5)

update_task_list()

root.mainloop()
