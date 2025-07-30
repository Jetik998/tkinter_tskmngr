from ui import UI
from logic import Logic
from controller import Controller
import os

if os.path.exists("data.json"):
    os.remove("data.json")
if __name__ == "__main__":
    ui = UI()
    logic = Logic()
    controller = Controller(ui, logic)
    ui.root.mainloop()
