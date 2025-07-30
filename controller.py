class Controller:
    def __init__(self, ui, logic):
        self.ui = ui
        self.logic = logic
        self._bind_events()
        self.load_treeview()

    def save_task(self):
        self.ui.main_window.frame1.edit_task_btn(text="Добавить")
        name = self.ui.main_window.frame1.entry.get()
        priority = self.ui.main_window.frame1.combo.get()
        deadline = self.ui.main_window.frame1.date_entry.get()
        self.logic.validator.validate_inputs(name, priority)
        self.ui.main_window.frame1.reset_inputs()
        task = self.logic.task.create_task(name, priority, deadline)
        task = self.logic.task.obj_to_dict(task)
        self.logic.data.new_task(task)
        self.ui.main_window.frame2.clear_tree()
        self.load_treeview()

    def load_treeview(self):
        data = self.logic.data.load_data(self.logic.data.filename)
        if data:
            for task in data:
                self.ui.main_window.frame2.add_to_treeview(task)

    def delete_task(self):
        selected = self.ui.main_window.frame2.selected_task
        self.logic.data.delete_task(selected)
        self.ui.main_window.frame2.clear_tree()
        self.load_treeview()

    def edit_task(self):
        name = self.ui.main_window.frame1.entry.get()
        self.logic.validator.validate_edit_task(name)
        selected = self.ui.main_window.frame2.selected_task
        task = self.logic.data.edit_task(selected)
        self.ui.main_window.frame2.clear_tree()
        self.load_treeview()
        self.ui.main_window.frame1.set_inputs(task)
        self.ui.main_window.frame1.edit_task_btn(text="Применить")

    def _bind_events(self):
        self.ui.main_window.frame1.btn.config(command=self.save_task)
        self.ui.main_window.frame2.btn_del.config(command=self.delete_task)
        self.ui.main_window.frame2.btn_edit.config(command=self.edit_task)
