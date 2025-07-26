class Controller:
    def __init__(self, ui, logic):
        self.ui = ui
        self.logic = logic
        self._bind_events()


    def add_task(self):
        name = self.ui.frame.entry.get()
        priority = self.ui.frame.combo.get()
        deadline = self.ui.frame.date_entry.get()
        self.logic.data.add_task(name, priority, deadline)

    def _bind_events(self):
        self.ui.frame.btn.config(command=self.add_task)



