import tkinter as tk
from tkinter import ttk

data = [
    {"id": 1, "name": "Alice", "role": "Developer"},
    {"id": 2, "name": "Bob", "role": "Designer"},
    {"id": 3, "name": "Charlie", "role": "Manager"},
    {"id": 4, "name": "Diana", "role": "Developer"},
]

def update_table(filter_text=""):
    # Очистить таблицу
    for row in tree.get_children():
        tree.delete(row)
    # Добавить отфильтрованные данные
    for item in data:
        if filter_text.lower() in item["name"].lower():
            tree.insert("", "end", values=(item["id"], item["name"], item["role"]))

def on_filter_change(*args):
    text = filter_var.get()
    update_table(text)

root = tk.Tk()
root.title("Фильтрация данных в таблице")

# Поле фильтра
filter_var = tk.StringVar()
filter_var.trace_add("write", on_filter_change)
tk.Entry(root, textvariable=filter_var).pack(padx=10, pady=5)

# Таблица (Treeview)
columns = ("id", "name", "role")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col.title())
    tree.column(col, width=100)
tree.pack(fill="both", expand=True, padx=10, pady=5)

update_table()

root.mainloop()
