class Controller:
    def __init__(self, ui, logic):
        self.ui = ui
        self.logic = logic
        self._bind_events()
        self.load_treeview()

    def save_task(self):
        name = self.ui.frame1.entry.get()
        priority = self.ui.frame1.combo.get()
        deadline = self.ui.frame1.date_entry.get()
        self.ui.frame1.reset_inputs()
        task = self.logic.task.create_task(name, priority, deadline)
        task = self.logic.task.obj_to_dict(task)
        self.logic.data.new_task(task)
        self.ui.frame2.clear_tree()
        self.load_treeview()

    def load_treeview(self):
        data = self.logic.data.load_data(self.logic.data.filename)
        if data:
            for task in data:
                self.ui.frame2.add_to_treeview(task)

    def delete_task(self):
        selected = self.ui.frame2.selected_task
        self.logic.data.delete_task(selected)
        self.ui.frame2.clear_tree()
        self.load_treeview()

    def _bind_events(self):
        self.ui.frame1.btn.config(command=self.save_task)
        self.ui.frame2.btn_del.config(command=self.delete_task)
