class Controller:
    def __init__(self, ui, logic):
        self.ui = ui
        self.logic = logic
        self._bind_events()


    def save_task(self):
        name = self.ui.frame1.entry.get()
        priority = self.ui.frame1.combo.get()
        deadline = self.ui.frame1.date_entry.get()
        self.ui.frame1.reset_inputs()
        task = self.logic.task.create_task(name, priority, deadline)
        self.logic.data.new_task(task)



    def _bind_events(self):
        self.ui.frame1.btn.config(command=self.save_task)



