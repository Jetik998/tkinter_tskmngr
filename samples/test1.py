import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Презентация контейнеров в Tkinter")
root.geometry("600x400")
root.configure(bg="lightgray")

# ---------- 1. Frame ----------
frame_section = tk.Frame(root, bg="white", bd=2, relief="groove")
frame_section.pack(padx=10, pady=10, fill="x")

tk.Label(frame_section, text="Frame — простой контейнер", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", padx=10, pady=5)
frame = tk.Frame(frame_section, bg="lightblue", height=50)
frame.pack(fill="x", padx=10, pady=5)

tk.Button(frame, text="Кнопка 1").pack(side="left", padx=10, pady=10)
tk.Button(frame, text="Кнопка 2").pack(side="left", padx=10, pady=10)


# ---------- 2. LabelFrame ----------
labelframe_section = tk.Frame(root, bg="white", bd=2, relief="groove")
labelframe_section.pack(padx=10, pady=10, fill="x")

tk.Label(labelframe_section, text="LabelFrame — контейнер с заголовком", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", padx=10, pady=5)
labelframe = tk.LabelFrame(labelframe_section, text="Настройки", bg="white")
labelframe.pack(fill="x", padx=10, pady=5)

tk.Checkbutton(labelframe, text="Включить звук").pack(anchor="w", padx=10, pady=2)
tk.Checkbutton(labelframe, text="Включить уведомления").pack(anchor="w", padx=10, pady=2)


# ---------- 3. PanedWindow ----------
paned_section = tk.Frame(root, bg="white", bd=2, relief="groove")
paned_section.pack(padx=10, pady=10, fill="both", expand=True)

tk.Label(paned_section, text="PanedWindow — контейнер с делителями", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", padx=10, pady=5)

paned = ttk.PanedWindow(paned_section, orient="horizontal")
paned.pack(fill="both", expand=True, padx=10, pady=5)

left = tk.Frame(paned, bg="#d0f0c0", width=200, height=100)
right = tk.Frame(paned, bg="#f0d0c0", width=200, height=100)

paned.add(left, weight=1)
paned.add(right, weight=1)

tk.Label(left, text="Левая панель", bg="#d0f0c0").pack(padx=10, pady=10)
tk.Label(right, text="Правая панель", bg="#f0d0c0").pack(padx=10, pady=10)


root.mainloop()
