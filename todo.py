import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("400x500")
root.config(bg="lightblue")

tasks = []  # List to store tasks

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to remove a task
def remove_task():
    try:
        selected_task = task_listbox.curselection()[0]
        tasks.pop(selected_task)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

# Function to mark a task as completed
def complete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        tasks[selected_task] = "✔ " + tasks[selected_task]  # Mark as completed
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to complete!")

# Function to update the listbox
def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Creating UI Elements
task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=10, padx=20, fill=tk.X)

add_button = tk.Button(root, text="Add Task", command=add_task, font=("Arial", 12), bg="green", fg="white")
add_button.pack(pady=5, padx=20, fill=tk.X)

task_listbox = tk.Listbox(root, font=("Arial", 14), height=10)
task_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

complete_button = tk.Button(root, text="Complete Task", command=complete_task, font=("Arial", 12), bg="blue", fg="white")
complete_button.pack(pady=5, padx=20, fill=tk.X)

remove_button = tk.Button(root, text="Remove Task", command=remove_task, font=("Arial", 12), bg="red", fg="white")
remove_button.pack(pady=5, padx=20, fill=tk.X)

exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12), bg="gray", fg="white")
exit_button.pack(pady=5, padx=20, fill=tk.X)

# Start the Tkinter event loop
root.mainloop()
