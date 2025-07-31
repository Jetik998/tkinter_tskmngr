import tkinter as tk

def change_font():
    print(f"Выбран шрифт: {font_var.get()}")

root = tk.Tk()
root.title("Многоуровневое меню")

menubar = tk.Menu(root)

font_var = tk.StringVar(value="Arial")

# Меню "Настройки"
settings_menu = tk.Menu(menubar, tearoff=0)

# Подменю "Шрифт" внутри "Настроек"
font_menu = tk.Menu(settings_menu, tearoff=0)

fonts = ["Arial", "Times New Roman", "Courier New", "Verdana"]
for f in fonts:
    font_menu.add_radiobutton(label=f, variable=font_var, value=f, command=change_font)

# Добавляем подменю "Шрифт" в меню "Настройки"
settings_menu.add_cascade(label="Шрифт", menu=font_menu)

# Можно добавить другие пункты в "Настройки"
settings_menu.add_command(label="Цвета", command=lambda: print("Открыть цвета"))

# Добавляем главное меню "Настройки" в строку меню
menubar.add_cascade(label="Настройки", menu=settings_menu)

root.config(menu=menubar)
root.mainloop()
