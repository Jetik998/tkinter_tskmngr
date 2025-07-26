import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tasklist")
        self.root.geometry("1280x960")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TLabel", font=("Segoe UI", 10), padding=5, background=self.root.cget("background"))
        self.style.configure("TEntry", font=("Segoe UI", 10), padding=5)
        self.style.configure("TCombobox", font=("Segoe UI", 10), padding=5, background=self.root.cget("background"))

        self.frame1 = MyFrame1(root)
        self.frame1.pack(padx=10, pady=150)
        self.frame2 = MyFrame2(root)
        self.frame2.pack(padx=10, pady=100)




class MyFrame1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.label = ttk.Label(self, text="Название задачи")
        self.label.grid(row=0, column=0, padx=5, pady=5)
        self.entry = ttk.Entry(self, width=30)
        self.entry.grid(row=1, column=0, padx=5, pady=5)

        self.label_combo = ttk.Label(self, text="Приоритет")
        self.label_combo.grid(row=0, column=1, padx=5, pady=5)
        self.combo = ttk.Combobox(self, values=["Критично", "Важно", "Нормально", "Не важно"], width=15)
        self.combo.grid(row=1, column=1, padx=5, pady=5)

        self.label_date = ttk.Label(self, text="Приоритет")
        self.label_date.grid(row=0, column=2, padx=5, pady=5)
        self.date_entry = DateEntry(self)
        self.date_entry.grid(row=1, column=2, padx=5, pady=5)

        self.btn = ttk.Button(self, text="Добавить")
        self.btn.grid(row=1, column=3, padx=5, pady=5)

class MyFrame2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.tree = ttk.Treeview(self, columns=("name", "priority", "date"), show="headings")
        self.tree.heading("name", text="Задача")
        self.tree.heading("priority", text="Приоритет")
        self.tree.heading("date", text="Дедлайн")
        self.tree.grid(row=3, column=0, padx=5, pady=5)
        self.tree.bind("<ButtonRelease-1>", )


