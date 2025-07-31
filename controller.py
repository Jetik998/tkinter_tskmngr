class Controller:
    def __init__(self, ui, logic):
        self.ui = ui
        self.logic = logic
        self.frame1 = self.ui.main_window.frame1
        self.frame2 = self.ui.main_window.frame2
        self.menu = self.ui.menu
        self._bind_events()
        self.load_treeview()


    def save_task(self):
        self.frame1.edit_task_btn(text="Добавить")
        name = self.frame1.entry.get()
        priority = self.frame1.combo.get()
        deadline = self.frame1.date_entry.get()
        self.logic.validator.validate_inputs(name, priority)
        self.frame1.reset_inputs()
        self.frame2.show_btn_edit()
        task = self.logic.task.create_task(name, priority, deadline)
        task = self.logic.task.obj_to_dict(task)
        self.logic.data.new_task(task)
        self.frame2.clear_tree()
        self.load_treeview()

    def load_treeview(self):
        data = self.logic.data.load_data(self.logic.data.filename)
        if data:
            for task in data:
                self.frame2.add_to_treeview(task)

    def delete_task(self):
        selected = self.frame2.selected_task
        self.logic.data.delete_task(selected)
        self.frame2.clear_tree()
        self.load_treeview()
        self.frame2.hide_change_btns()


    def edit_task(self):
        name = self.frame1.entry.get()
        self.logic.validator.validate_edit_task(name)
        selected = self.frame2.selected_task
        task = self.logic.data.edit_task(selected)
        self.frame2.clear_tree()
        self.load_treeview()
        self.frame1.set_inputs(task)
        self.frame1.edit_task_btn(text="Применить")
        self.frame2.hide_btn_edit()

    def _bind_events(self):
        self.frame1.btn.config(command=self.save_task)
        self.frame2.btn_yes.config(command=self.delete_task)
        self.frame2.btn_edit.config(command=self.edit_task)
