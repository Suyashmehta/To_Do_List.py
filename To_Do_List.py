import tkinter as tk
from tkinter import messagebox

# GUI :
root = tk.Tk()
root.title("To-Do List")
root.geometry("1000x600")
root.config(bg="#1e1e1e")  #Dark theme

tasks = []

# Function
def add_task():
    task = task_entry.get("1.0", tk.END).strip()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete("1.0", tk.END) # clear box
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        listbox.delete(selected)
    except:
        messagebox.showwarning("None Task Entered", "Please select a task to remove!")

# Title Label
label = tk.Label(root, text="My To-Do List", font=("Segoe UI", 16, "bold"), bg="#1e1e1e", fg="white")
label.pack(pady=10)

task_entry = tk.Text(
    root,
    height=3, width=55,
    font=("Segoe UI", 12),
    bg="#2d2d2d", fg="White",
    bd=3, relief="raised",
    insertbackground="white"   # cursor white color
)
task_entry.pack(pady=10)

# Add & Remove sections
add_button = tk.Button(root, text="Add Task", command=add_task, font=("Segoe UI", 12), bg="#FB8C00", fg="Black", relief="raised", bd=5)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task, font=("Segoe UI", 12), bg="#E53935", fg="Black", relief="raised", bd=3)
remove_button.pack(pady=5)

# List and Border
listbox = tk.Listbox(
    root,
    height=25, width=50,
    font=("Consolas", 12),
    bg="#2d2d2d", fg="white",
    bd=2, relief="solid",
    selectbackground="#555"  #Listbox cursor White
)
listbox.pack(pady=10)

root.mainloop()
