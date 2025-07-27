from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("To-Do List")
root.geometry("400x450")

tasks = []  # Store tasks in memory


def add_task():
    task_string = task_field.get()
    if len(task_string.strip()) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        list_update()
        task_field.delete(0, END)

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert(END, task)

def delete_task():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        if selected_task in tasks:
            tasks.remove(selected_task)
            list_update()
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    confirm = messagebox.askyesno("Delete All", "Are you sure?")
    if confirm:
        task_listbox.delete(0, END)
        tasks.clear()

def clear_list():
    task_listbox.delete(0, END)


task_label = Label(root, text="Enter Task:", font=('Arial', 12))
task_label.pack(pady=10)

task_field = Entry(root, width=30, font=('Arial', 12))
task_field.pack(pady=5)

add_button = Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

delete_button = Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

delete_all_button = Button(root, text="Delete All Tasks", width=20, command=delete_all_tasks)
delete_all_button.pack(pady=5)

task_listbox = Listbox(root, height=10, width=40, font=('Arial', 12))
task_listbox.pack(pady=10)


list_update()
root.mainloop()
