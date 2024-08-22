import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You need to enter a task.")

# Function to mark a task as completed (strikethrough)
def mark_completed():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(selected_task_index, "✔ " + task)
        tasks_listbox.itemconfig(selected_task_index, {'fg': 'gray'})
        tasks_listbox.itemconfig(selected_task_index, {'font': 'Helvetica 10 italic'})

# Function to delete a task from the list
def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "You need to select a task.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create the entry box for new tasks
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Add Task button
add_task_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_task_button.pack(side=tk.LEFT, padx=10)

# Mark Completed button
mark_completed_button = tk.Button(button_frame, text="Mark Completed", command=mark_completed)
mark_completed_button.pack(side=tk.LEFT, padx=10)

# Delete Task button
delete_task_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_task_button.pack(side=tk.LEFT, padx=10)

# Create a listbox to display the tasks
tasks_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
tasks_listbox.pack(pady=20)

# Run the main event loop
root.mainloop()