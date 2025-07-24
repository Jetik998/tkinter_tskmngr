import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tasklist")
        self.geometry("1280x960")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TLabel", font=("Segoe UI", 10), padding=5, background=self.cget("background"))
        self.style.configure("TEntry", font=("Segoe UI", 10), padding=5)
        self.style.configure("TCombobox", font=("Segoe UI", 10), padding=5, background=self.cget("background"))

        self.frame = MyFrame(self)
        self.frame.pack(padx=10, pady=200)

class MyFrame(tk.Frame):
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


