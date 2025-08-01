import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Меню с подменю")


        menubar = tk.Menu(root)
        root.config(menu=menubar)


        self.editmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Правка", menu=self.editmenu)



        self.editmenu.add_command(label="Обычное действие", command=self.do_something)



        self.fonts_menu = tk.Menu(self.editmenu, tearoff=0)


        for f in ["Arial", "Courier", "Times New Roman", "Comic Sans MS"]:
            self.fonts_menu.add_command(label=f, command=lambda f=f: self.set_font(f))



        self.editmenu.add_cascade(label="Шрифт", menu=self.fonts_menu)


    def do_something(self):
        print("Выполнено обычное действие!")

    def set_font(self, font_name):
        print(f"Выбран шрифт: {font_name}")

root = tk.Tk()
app = App(root)
root.mainloop()
