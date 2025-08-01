class Controller:
    def __init__(self, ui, logic):
        self.ui = ui
        self.logic = logic
        self.frame1 = self.ui.main_window.frame1
        self.frame2 = self.ui.main_window.frame2
        self.menu = self.ui.menu
        self.main_window = self.ui.main_window
        self._bind_events()
        self.load_treeview()

        self.ui.menu.on_font_change = self.change_serif

    # Создание и добавление задачи
    def save_task(self):
        """
        Создаёт новую задачу и добавляет её в список.

        Считывает данные из полей ввода, валидирует их,
        очищает поля, создаёт объект задачи и преобразует его в словарь,
        добавляет задачу в хранилище, обновляет отображение списка задач
        и показывает кнопки "Удалить" и "Изменить".
        """
        self.frame1.change_text_btn(arg="Добавить")
        name = self.frame1.entry.get()
        priority = self.frame1.combo.get()
        deadline = self.frame1.date_entry.get()
        self.logic.validator.validate_inputs(name, priority)
        self.frame1.reset_inputs()
        task = self.logic.task.create_task(name, priority, deadline)
        task = self.logic.task.obj_to_dict(task)
        self.logic.data.new_task(task)
        self.frame2.clear_tree()
        self.load_treeview()
        self.frame2.show_buttons(self.frame2.btn_del, self.frame2.btn_edit)

    def load_treeview(self):
        """
        Загружает задачи из файла и отображает их в TreeView.

        Если данные есть, добавляет каждую задачу в список на экране.
        """
        data = self.logic.data.load_data(self.logic.data.filename)
        if data:
            for task in data:
                self.frame2.add_to_treeview(task)

    def validate_selection(self):
        """
        Проверяет, выбрана ли задача в TreeView.

        Если задача не выбрана — выводит сообщение об ошибке.
        Если выбрана — скрывает кнопки "Удалить" и "Изменить" и показывает кнопки "Да" и "Нет" для подтверждения удаления.
        """
        selected = self.frame2.selected_task
        self.logic.validator.validate_edit_task(selected, arg="Удалить")
        self.frame2.on_btn_del()

    def delete_task(self):
        """
        Удаляет выбранные задачи.

        Получает выбранные ID задач,
        удаляет их из данных через логику,
        очищает и обновляет отображение в TreeView,
        а также переключает видимость кнопок после удаления.
        """
        selected = self.frame2.selected_task
        self.logic.data.delete_task(selected)
        self.frame2.clear_tree()
        self.load_treeview()
        self.frame2.on_btn_del()

    def edit_task(self):
        """
        Обрабатывает редактирование выбранной задачи.

        Если задача выбрана:
        - скрывает кнопки "Изменить" и "Удалить" для предотвращения повторных действий;
        - заполняет поля ввода данными выбранной задачи;
        - меняет текст кнопки "Добавить" на "Изменить", чтобы указать режим редактирования;
        - удаляет выбранную задачу из списка и отображения (TreeView).

        Редактирование реализовано через удаление старой задачи и подготовку формы для создания обновлённой задачи.
        После сохранения изменений кнопка возвращается в состояние "Добавить".
        """
        selected = self.frame2.selected_task
        self.logic.validator.validate_edit_task(selected, arg="Изменить")
        self.frame2.buttons(self.frame2.btn_del, self.frame2.btn_edit)
        self.frame1.change_text_btn(arg="Изменить")
        task = self.logic.data.edit_task(selected)
        self.frame2.clear_tree()
        self.load_treeview()
        self.frame1.set_inputs(task)

    def change_serif(self, serif):
        self.main_window.edit_serif(serif)

    def _bind_events(self):
        self.frame1.btn.config(command=self.save_task)
        self.frame2.btn_yes.config(command=self.delete_task)
        self.frame2.btn_edit.config(command=self.edit_task)
        self.frame2.btn_del.config(command=self.validate_selection)

