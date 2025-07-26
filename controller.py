class Controller:
    def __init__(self, ui, logic):
        self.ui = ui
        self.logic = logic
        self._bind_events()


    def add_task(self):
        name = self.ui.frame1.entry.get()
        priority = self.ui.frame1.combo.get()
        deadline = self.ui.frame1.date_entry.get()
        self.logic.data.add_task(name, priority, deadline)

    def _bind_events(self):
        self.ui.frame1.btn.config(command=self.add_task)



