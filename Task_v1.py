
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from tkinter import END
from dataclasses import dataclass
import json







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
    data_cache = []

def add_task():
    pass
    global task_list


def add_task():
    name = entry.get()
    priority = combo.get()
    deadline = date_entry.get()
    task = Task(name, priority, deadline)
    print(task)
    Data.data.append(task)

# Интерфейс

root = tk.Tk()
root.title("Шаблоны популярных виджетов Tkinter")
root.geometry("1280x960")

frame = ttk.Frame(root) #Первый блок
frame.pack(padx=10, pady=10)

#Шаг 1 (Название задачи)
label = ttk.Label(frame, text="Создать задачу")
label.pack(padx=10, pady=10)
entry = ttk.Entry(frame, width=20)
entry.pack(padx=10, pady=10, side=tk.LEFT)
label1 = ttk.Label(frame, text="Создать задачу")
label1.pack(padx=10, pady=10)
label2 = ttk.Label(frame, text="Создать задачу")
label2.pack(padx=10, pady=10)
label3 = ttk.Label(frame, text="Создать задачу")
label3.pack(padx=10, pady=10)
combo = ttk.Combobox(frame, values=["Критично", "Важно", "Нормально", "Не важно"])
combo.pack(padx=10, pady=10, side=tk.LEFT)
date_entry = DateEntry(frame)
date_entry.pack(padx=10, pady=10, side=tk.LEFT)
btn = ttk.Button(frame, text="Добавить", command=add_task)
btn.pack(padx=10, pady=10)




tree = ttk.Treeview(root, columns=("name", "priority", "date"), show="headings")
tree.heading("name", text="Задача")
tree.heading("priority", text="Приоритет")
tree.heading("date", text="Дедлайн")
#tree.pack(expand=True, fill="both")
tree.bind("<ButtonRelease-1>", )


root.mainloop()