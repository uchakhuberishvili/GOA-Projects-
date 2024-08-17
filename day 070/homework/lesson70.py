import tkinter as tk
from tkinter import messagebox

tasks = []

def update_listbox():

    listbox_tasks.delete(0, tk.END)

    for index, task in enumerate(tasks, start=1):
        listbox_tasks.insert(tk.END, f"{index}. {task}")

    label_task_count.config(text=f"Total tasks: {len(tasks)}")

def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        tasks.pop(selected_task_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")


Program = tk.Tk()
Program.title("My Tasks")


Program.configure(bg='light Gray')


frame = tk.Frame(Program, bg='gray', bd=2, relief=tk.RAISED)
frame.pack(pady=30, padx=20)


entry_task = tk.Entry(frame, width=60, bg='light gray', bd=2)
entry_task.pack(side=tk.LEFT, padx=10, pady=10)


button_add = tk.Button(frame, text="Add", command=add_task, bg='lightblue', bd=3)
button_add.pack(side=tk.LEFT, padx=10, pady=15)


button_delete = tk.Button(frame, text="Delete", command=delete_task, bg='lightcoral', bd=3)
button_delete.pack(side=tk.LEFT, padx=5, pady=5)


listbox_tasks = tk.Listbox(Program, width=70, height=30, bg='light gray', bd=2, selectmode=tk.SINGLE, relief=tk.RAISED)
listbox_tasks.pack(pady=20, padx=20)


label_task_count = tk.Label(Program, text="Total tasks: 0", bg='lightgrey', font=('Helvetica', 12))
label_task_count.pack(pady=10)


Program.mainloop()




# Themes: silver,

# Main: light gray
# user input:dark gray , charcoal
# user input frame: white with black test
# list box: silver
# buttons: light blue for "add" and light red for "delete" , cyan for "add" and for "delete" burgundy