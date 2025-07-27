from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("To-Do List")
root.geometry("400x500")

tasks = []

def add_tasks():
    task_string = tasks_field.get()
    if len(task_string.strip()) == 0:
        messagebox.showinfo('Error', 'Field is Empty. Cannot add task.')
    else:
        tasks.append(task_string)
        list_update()
        tasks_field.delete(0, END)

def update_tasks():
    try:
        selected_index = tasks_listbox.curselection()[0]
        updated_task = tasks_field.get().strip()

        if updated_task == "":
            messagebox.showinfo("Error", "Task cannot be empty!")
            return

        tasks[selected_index] = updated_task
        list_update()
        tasks_field.delete(0, END)
    except:
        messagebox.showinfo('Error', 'No Task Selected. Do Not Delete Task')


def list_update():
    clear_list()
    for task in tasks:
        tasks_listbox.insert(END, task)


def delete_tasks():
    try:
        selected_task = tasks_listbox.get(tasks_listbox.curselection())
        if selected_task in tasks:
            tasks.remove(selected_task)
            list_update()
    except:
        messagebox.showinfo('Error', 'No Task Selected. Do Not Delete Task')

def delete_all_tasks():
    confirm = messagebox.askyesno("Delete All Tasks", "Do You Agree for Delete All Tasks")
    if confirm:
        tasks_listbox.delete(0, END)
        tasks.clear()

def clear_list():
    tasks_listbox.delete(0, END)


tasks_label = Label(root, text="ENTER TASKS:", font=('Arial', 14))
tasks_label.pack(pady=12)

tasks_field = Entry(root, width=35, font=('Arial', 14))
tasks_field.pack(pady=6)

add_button = Button(root, text="ADD TASK", width=20, command=add_tasks)
add_button.pack(pady=6)

delete_button = Button(root, text="DELETE TASK", width=20, command=delete_tasks)
delete_button.pack(pady=6)

delete_all_button = Button(root, text="DELETE ALL TASKS", width=20, command=delete_all_tasks)
delete_all_button.pack(pady=6)

update_button = Button(root, text="UPDATE TASK", width=20, command=update_tasks)
update_button.pack(pady=6)

tasks_listbox = Listbox(root, height=10, width=40, font=('Arial', 12))
tasks_listbox.pack(pady=10)

list_update()

root.mainloop()
