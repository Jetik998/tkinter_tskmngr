import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import END


class Task:
    def __init__(self, name=None, priority=None, deadline=None):
        self.name = name
        self.priority = priority
        self.deadline = deadline

    def __str__(self):
        return f"{self.name} {self.priority} {self.deadline}"

    def __repr__(self):
        return f"{self.name} {self.priority} {self.deadline}"


class Data:
    data = []


def add_task():
    global task_list


task_list = []

step_1_str = ""


def step_1(*args):  # Ввод в поле
    global var, step_1_str
    step_1_str = var.get()
    if step_1_str == "":
        btn_step_1.pack_forget()
    else:
        btn_step_1.pack()


def step_1_btn():  # Перенос из поля в lst_add_task
    global step_1_str, task_list
    task_list.append(step_1_str)
    entry.delete(0, END)
    entry.pack_forget()
    label.pack_forget()
    label_2.pack(padx=10, pady=10)
    combo.pack(padx=10, pady=10)


def step_2_btn(event):  # Появление кнопки по выбору
    btn_step_2.pack()


def step_2():
    global task_list
    priority = combo.get()
    task_list.append(priority)
    label_2.pack_forget()
    combo.pack_forget()
    btn_step_2.forget()
    label_3.pack()
    date_entry.pack()


def step_3_btn(event):  # Появление кнопки по выбору
    btn_step_3.pack()


def step_3():
    global task_list
    date = date_entry.get()
    task_list.append(date)
    create_task()
    label_3.pack_forget()
    date_entry.pack_forget()
    btn_step_3.forget()
    label_4.config(text="Задача добавлена!")
    label_4.pack(padx=10, pady=10)
    frame.after(700, label4_timer)


def label4_timer():  # Конец цикла
    label_4.pack_forget()


def create_task():
    global task_list
    name = task_list[0]
    priority = task_list[1]
    deadline = task_list[2]
    d = [n.zfill(2) for n in deadline.split("/")]
    deadline = ".".join([d[1], d[0], d[2]])
    task = Task(name, priority, deadline)
    print(task)
    Data.data.append(task)


# Интерфейс

root = tk.Tk()
root.title("Шаблоны популярных виджетов Tkinter")
root.geometry("1280x960")

frame = ttk.Frame(root)  # Первый блок
frame.pack(padx=10, pady=10, fill="x")

# Шаг 1 (Название задачи)
label = ttk.Label(frame, text="Введите название задачи")
label.pack(padx=10, pady=10)
var = tk.StringVar()
var.trace_add("write", step_1)
entry = ttk.Entry(frame, width=20, textvariable=var)
entry.pack(padx=10, pady=10)
btn_step_1 = ttk.Button(frame, text="Добавить", command=step_1_btn)
# Шаг 2 (Выбор приоритета)
label_2 = ttk.Label(frame, text="Выберите приоритет")
combo = ttk.Combobox(frame, values=["Критично", "Важно", "Нормально", "Не важно"])
combo.bind("<<ComboboxSelected>>", step_2_btn)
btn_step_2 = ttk.Button(frame, text="Добавить", command=step_2)
# Шаг 3 (Выбор даты)
date_entry = DateEntry(frame)
date_entry.bind("<<DateEntrySelected>>", step_3_btn)
label_3 = ttk.Label(frame, text="Установите дедлайн")
btn_step_3 = ttk.Button(frame, text="Добавить", command=step_3)
label_4 = ttk.Label(frame)


tree = ttk.Treeview(root, columns=("name", "priority", "date"), show="headings")
tree.heading("name", text="Задача")
tree.heading("priority", text="Приоритет")
tree.heading("date", text="Дедлайн")
# tree.pack(expand=True, fill="both")
tree.bind(
    "<ButtonRelease-1>",
)


root.mainloop()
