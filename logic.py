import json
import os
from typing import Dict, List, Union, Optional, Any, Type, Tuple
from tkinter import messagebox


class Task:

    def __init__(
        self,
        name: Optional[str] = None,
        priority: Optional[str] = None,
        deadline: Optional[str] = None,
    ):
        self.name = name
        self.priority = priority
        self.deadline = deadline
        self.id = None

    def __str__(self):
        return f"{self.name} {self.priority} {self.deadline}"

    def __repr__(self):
        return f"{self.name} {self.priority} {self.deadline}"

    @classmethod
    def create_task(
        cls: Type["Task"], name: str, priority: str, deadline: str
    ) -> object:
        """
        Создаёт и возвращает новый объект задачи.

        Принимает имя, приоритет и дедлайн,
        создаёт экземпляр класса Task и возвращает его.
        """
        task = Task(name=name, priority=priority, deadline=deadline)
        return task

    def obj_to_dict(self) -> dict:
        return {"name": self.name, "priority": self.priority, "deadline": self.deadline}


class Data:
    filename = "data.json"

    @classmethod
    def load_data(cls, filename: str) -> Any:
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    @classmethod
    def save_data(
        cls, filename: str, data: List[Union[Any, Dict[str, Union[str, int]]]]
    ) -> None:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            # print(json.dumps(data, ensure_ascii=False, indent=4))

    @classmethod
    def new_task(cls, task: object) -> None:
        """
        Добавляет новую задачу в список.

        Загружает текущие задачи из файла, добавляет новую задачу,
        перенумеровывает задачи, чтобы у каждой был уникальный и последовательный ID,
        и сохраняет обновлённый список обратно в файл.
        """
        data = cls.load_data(cls.filename)
        data.append(task)
        for index, item in enumerate(data, start=1):
            item["id"] = index
        cls.save_data(cls.filename, data)

    @classmethod
    def delete_task(cls, selected: Tuple[str, ...]) -> None:
        """
        Удаляет задачи с указанными ID из данных.

        Загружает текущие задачи из файла, фильтрует их,
        исключая задачи с ID из списка selected,
        и сохраняет обновлённый список обратно в файл.
        """
        data = cls.load_data(cls.filename)
        if data:
            data = [task for task in data if str(task["id"]) not in selected]
            cls.save_data(cls.filename, data)

    @classmethod
    def edit_task(cls, selected: Tuple[str, ...]) -> Dict[str, Any]:
        """
        Проверяет, что выбрана хотя бы одна задача.
        Загружает данные из файла, фильтрует задачи по выбранным ID,
        удаляет выбранные задачи и возвращает первую из них.
        """
        if not selected:
            messagebox.showerror("Ошибка", "Выберите задачу")
            raise ValueError("Не выбрана задача")
        data = cls.load_data(cls.filename)
        if data:
            task = [task for task in data if str(task["id"]) in selected]
            Data.delete_task(selected)
            return task[0]

class InputValidator:

    @staticmethod
    def validate_inputs(name: str, priority: str):
        """Проверяет, что обязательные поля заполнены."""
        if not name:
            messagebox.showerror("Ошибка", "Введите название задачи")
            raise ValueError("Название задачи не может быть пустым")
        if not priority:
            messagebox.showerror("Ошибка", "Введите приоритет")
            raise ValueError("Приоритет не может быть пустым")
    @staticmethod
    def validate_edit_task(selected: Tuple[str, ...], arg="") -> None:
        """Проверяет, что задача выбрана."""
        if arg == "Изменить":
            if not selected:
                messagebox.showerror("Ошибка", "Не выбрана задача для редактирования")
                raise ValueError("Не выбрана задача для изменения")
        elif arg == "Удалить":
            if not selected:
                messagebox.showerror("Ошибка", "Не выбрана задача для удаления")
                raise ValueError("Не выбрана задача для изменения")


class Logic:
    def __init__(self):
        self.task = Task
        self.data = Data()
        self.validator = InputValidator()
