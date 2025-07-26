import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry  # Для выбора даты нужно установить библиотеку tkcalendar

def next_step_1():
    # Получаем значение из первого Entry
    value1 = entry1.get()
    print("Введено:", value1)
    # Показываем второй этап (combobox)
    entry1.pack_forget()
    btn1.pack_forget()
    combo.pack()
    btn2.pack()

def next_step_2():
    # Получаем выбранный вариант из combobox
    value2 = combo.get()
    print("Выбран:", value2)
    # Показываем третий этап (выбор даты)
    combo.pack_forget()
    btn2.pack_forget()
    date_entry.pack()
    btn3.pack()

def finish():
    # Получаем выбранную дату
    value3 = date_entry.get_date()
    print("Дата:", value3)
    root.quit()

root = tk.Tk()
root.title("Многоэтапный ввод")

# Этап 1: Entry
entry1 = tk.Entry(root)
entry1.pack()

btn1 = tk.Button(root, text="Далее", command=next_step_1)
btn1.pack()

# Этап 2: Combobox
combo = ttk.Combobox(root, values=["Вариант 1", "Вариант 2", "Вариант 3"])

btn2 = tk.Button(root, text="Далее", command=next_step_2)

# Этап 3: Выбор даты
date_entry = DateEntry(root)

btn3 = tk.Button(root, text="Готово", command=finish)

root.mainloop()
