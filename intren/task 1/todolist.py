import tkinter as tk
from tkinter import messagebox

# Function to add a new task to the list
def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to update a selected task
def update_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        updated_task = entry.get()
        if updated_task:
            task_list.delete(selected_task_index)
            task_list.insert(selected_task_index, updated_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")
    else:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Function to delete a selected task
def delete_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main application window
root = tk.Tk()
root.title("To-Do List")

# Create a task list
task_list = tk.Listbox(root)
task_list.pack(pady=10)

# Create an entry field for task input
entry = tk.Entry(root)
entry.pack(pady=10)

# Create buttons for adding, updating, and deleting tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
update_button = tk.Button(root, text="Update Task", command=update_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)

add_button.pack(pady=5)
update_button.pack(pady=5)
delete_button.pack(pady=5)

# Run the Tkinter main loop
root.mainloop()
