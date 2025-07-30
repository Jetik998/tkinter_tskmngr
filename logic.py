import json
import os
from typing import Dict, List, Union, Optional, Any, Type, Tuple
from datetime import datetime
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
        task = Task(name=name, priority=priority, deadline=deadline)
        return task

    def obj_to_dict(self) -> dict:
        return {"name": self.name, "priority": self.priority, "deadline": self.deadline}


class Data:
    filename = "data.json"

    # Функция для выгрузки данных из файла
    @classmethod
    def load_data(cls, filename: str) -> Any:
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    # Функция для сохранения данных в файл
    @classmethod
    def save_data(
        cls, filename: str, data: List[Union[Any, Dict[str, Union[str, int]]]]
    ) -> None:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            print(json.dumps(data, ensure_ascii=False, indent=4))

    # Добавление задачи
    @classmethod
    def new_task(cls, task: object) -> None:
        data = cls.load_data(cls.filename)
        data.append(task)
        for index, item in enumerate(data, start=1):
            item["id"] = index
        cls.save_data(cls.filename, data)

    @classmethod
    def delete_task(cls, selected: Tuple[str, ...]) -> None:
        print(f"selected = {selected}")
        data = cls.load_data(cls.filename)
        if data:
            data = [task for task in data if str(task["id"]) not in selected]
            cls.save_data(cls.filename, data)


class InputValidator:
    @staticmethod
    def validate_inputs(name: str, priority: str):
        if not name:
            messagebox.showerror("Ошибка", "Введите название задачи")
            raise ValueError("Название задачи не может быть пустым")
        if not priority:
            messagebox.showerror("Ошибка", "Введите приоритет")
            raise ValueError("Приоритет не может быть пустым")


class Logic:
    def __init__(self):
        self.task = Task
        self.data = Data()
        self.validator = InputValidator()
