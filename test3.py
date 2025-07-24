import tkinter as tk
from dataclasses import dataclass
from tkinter import ttk, messagebox
import json




# Логика

class Task:
    def __init__(self, name=None, priority=None,deadline=None):
        self.name = name
        self.priority = priority
        self.deadline = deadline

    def __str__(self):
        return f'{self.name} {self.priority} {self.deadline}'
    def __repr__(self):
        return f'{self.name} {self.priority} {self.deadline}'
class Data:
    data = []




def save_json(data):
    pass


id_data = {}

def refresh_tasks():
    listbox.delete(0, tk.END)
    tree.delete(*tree.get_children())
    id_data.clear()
    for task in Data.data:
        listbox.insert(tk.END, task)
        row_id = tree.insert('', 'end', values=task)
        id_data[row_id] = task


step = 0
input_lst = []

def add_task():
    global input_lst, step
    value = entry.get()
    if value == "":
        messagebox.showerror("Ошибка", "Пустое поле")
    else:
        if step == 0:
            input_lst.append(value)
            entry.delete(0, tk.END)
            step = 1
            label.config(text="Введите приоритет")
            btn.config(text="Шаг 2 из 3")
        elif step == 1:
            input_lst.append(value)
            entry.delete(0, tk.END)
            step = 2
            label.config(text="Введите дедлайн")
            btn.config(text="Шаг 3 из 3")
        else:
            input_lst.append(value)
            entry.delete(0, tk.END)
            Data.data.append(Task(input_lst[0], input_lst[1], input_lst[2]))
            print(Data.data)
            input_lst = []
            step = 0
            label.config(text="Введите название задачи!")
            btn.config(text="Добавить")
            refresh_tasks()

def del_task():
    click = listbox.curselection()
    if not click:
        messagebox.showerror("Ошибка", "Выберите задачу которую нужно удалить")
    else:
        for i in click:
            del Data.data[i]
        refresh_tasks()


def get_id(event):
    global selected_id
    selected_id = tree.focus()

selected_id = None

def del_task2():
    if selected_id in id_data:
        for obj in Data.data:
            if obj == id_data[selected_id]:
                Data.data.remove(obj)
                refresh_tasks()
                break







# Интерфейс

root = tk.Tk()
root.title("Шаблоны популярных виджетов Tkinter")
root.geometry("1280x960")

label = ttk.Label(root, text="Введите название задачи!")
label.pack()

entry = ttk.Entry(root)
entry.pack()

btn = ttk.Button(root, text="Добавить", command=add_task)
btn.pack()

listbox = tk.Listbox(root, activestyle="none")
listbox.pack()

btn_del = ttk.Button(root, text="Удалить", command=del_task)
btn_del.pack()

btn_del2 = ttk.Button(root, text="Удалить", command=del_task2)
btn_del2.pack()

tree = ttk.Treeview(root, columns=("name", "priority", "date"), show="headings")
tree.heading("name", text="Задача")
tree.heading("priority", text="Приоритет")
tree.heading("date", text="Дедлайн")
tree.pack(expand=True, fill="both")
tree.bind("<ButtonRelease-1>", get_id)
root.mainloop()
#НОВАЯ ФИЧА