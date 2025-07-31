import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Tasklist")
        self.root.geometry("1280x960")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure(
            "TLabel",
            font=("Segoe UI", 10),
            padding=5,
            background=self.root.cget("background"),
        )
        self.style.configure("TEntry", font=("Segoe UI", 10), padding=5)
        self.style.configure(
            "TCombobox",
            font=("Segoe UI", 10),
            padding=5,
            background="white",  # фон выпадающего списка
            fieldbackground="white",  # фон текстового поля
            foreground="black",  # цвет текста
        )
        self.style.configure("Custom.Treeview", font=("Segoe UI", 12))
        self.style.configure("Custom.Treeview.Heading", font=("Segoe UI", 10))

        self.frame1 = MyFrame1(root)
        self.frame1.pack(padx=10, pady=0)
        self.frame2 = MyFrame2(root)
        self.frame2.pack(padx=10, pady=0)


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
        self.combo = ttk.Combobox(
            self,
            values=["Критично", "Важно", "Нормально", "Не важно"],
            width=15,
            state="readonly",
        )
        self.combo.grid(row=1, column=1, padx=5, pady=5)

        self.label_date = ttk.Label(self, text="Дедлайн")
        self.label_date.grid(row=0, column=2, padx=5, pady=5)
        self.date_entry = DateEntry(self, state="readonly", locale="ru_RU")
        self.date_entry.grid(row=1, column=2, padx=5, pady=5)

        self.btn = ttk.Button(self, text="Добавить")
        self.btn.grid(row=1, column=3, padx=5, pady=5)

    def reset_inputs(self):
        self.entry.delete(0, "end")
        self.combo.delete(0, "end")
        self.date_entry.delete(0, "end")

    def set_inputs(self, task):
        self.entry.insert(0, task["name"])
        self.combo.set(task["priority"])
        self.date_entry.set_date(task["deadline"])

    def edit_task_btn(self, text):
        if text == "Добавить":
            self.btn.config(text="Добавить")
        elif text == "Применить":
            self.btn.config(text="Изменить")


class MyFrame2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)  # borderwidth=3, relief="solid"
        self.parent = parent

        self.tree = ttk.Treeview(
            self,
            columns=("name", "priority", "date"),
            show="headings",
            style="Custom.Treeview",
        )
        self.selected_task = []
        self.tree.heading("name", text="Задача")
        self.tree.heading("priority", text="Приоритет")
        self.tree.heading("date", text="Дедлайн")
        self.tree.pack()
        self.tree.bind("<<TreeviewSelect>>", self.get_select_task)

        self.tree.column("name", anchor="center", width=200)
        self.tree.heading("name", text="Задача", anchor="center")
        self.tree.column("priority", anchor="center", width=200)
        self.tree.heading("priority", text="Приоритет", anchor="center")
        self.tree.column("date", anchor="center", width=200)
        self.tree.heading("date", text="Дедлайн", anchor="center")

        self.btn_del = ttk.Button(self, text="Удалить", command=self.del_change)
        self.btn_del.pack(side="right", padx=5, pady=5)

        self.btn_edit = ttk.Button(self, text="Изменить")
        self.btn_edit.pack(side="right", padx=5, pady=5)

        self.btn_no = ttk.Button(self, text="Нет", command=self.hide_change_btns)
        self.btn_yes = ttk.Button(self, text="Да")

    def clear_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def add_to_treeview(self, task):
        self.tree.insert(
            "",
            "end",
            iid=task["id"],
            values=(task["name"], task["priority"], task["deadline"]),
        )

    def get_select_task(self, event):
        self.selected_task = event.widget.selection()

    def selected_task(self):
        return self.selected_task

    def show_btn_edit(self):
        if not self.btn_edit.winfo_ismapped():
            self.btn_edit.pack(side="right", padx=5, pady=5)

    def hide_btn_edit(self):
        if self.btn_edit.winfo_ismapped():
            self.btn_edit.pack_forget()

    def show_btn_del(self):
        if not self.btn_del.winfo_ismapped():
            self.btn_del.pack(side="right", padx=5, pady=5)

    def hide_btn_del(self):
        if self.btn_del.winfo_ismapped():
            self.btn_del.pack_forget()

    def hide_change_btns(self):
        self.hide_buttons(self.btn_yes, self.btn_no)
        self.show_buttons(self.btn_edit, self.btn_del)

    def show_change_btns(self):
        self.show_buttons(self.btn_yes, self.btn_no) #

    def del_change(self):
        self.hide_buttons(self.btn_del,self.btn_edit)
        self.show_buttons(self.btn_yes,self.btn_no)


    def hide_buttons(self, *buttons):
        for b in buttons:
            b.pack_forget()

    def show_buttons(self, *buttons):
        for b in buttons:
            b.pack(side="right", padx=5, pady=5)


class Menu(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.menu = tk.Menu(self, tearoff=0)
        self.menu.add_command(label="Новый")
        self.menu.add_command(label="Открыть")
        self.menu.add_separator()
        self.menu.add_command(label="Выход")
        self.add_cascade(label="Файл", menu=self.menu)

        self.editmenu = tk.Menu(self, tearoff=0)
        self.editmenu.add_command(label="Стиль")
        self.editmenu.add_command(label="Шрифт")
        self.add_cascade(label="Настройки", menu=self.editmenu)



class UI:
    def __init__(self):
        self.root = tk.Tk()

        self.main_window = MainWindow(self.root)
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)