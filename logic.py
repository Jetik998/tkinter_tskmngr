import json
import os
from typing import Union, List, Dict, Any, Type



class Task:
    def __init__(self, name: str = None, priority: str = None,deadline: str = None):
        self.name = name
        self.priority = priority
        self.deadline = self._to_iso_date(deadline)
        self.id = None

    @staticmethod
    def _to_iso_date(raw_date: str) -> str:
        from datetime import datetime
        return datetime.strptime(raw_date, "%m/%d/%y").strftime("%Y-%m-%d")

    def __str__(self):
        return f'{self.name} {self.priority} {self.deadline}'

    def __repr__(self):
        return f'{self.name} {self.priority} {self.deadline}'

    @classmethod
    def create_task(cls: Type["Task"], name: str, priority: str, deadline: str) -> object:
        task = Task(name=name, priority=priority, deadline=deadline)
        return task

    def obj_to_dict(self) -> dict:
        return {
            'name': self.name,
            'priority': self.priority,
            'deadline': self.deadline
        }

class Data:
    filename = 'data.json'

    # Функция для выгрузки данных из файла
    @classmethod
    def load_data(cls, filename: str)-> Any:
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    # Функция для сохранения данных в файл
    @classmethod
    def save_data(cls, filename: str, data)-> None:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            print(json.dumps(data, ensure_ascii=False, indent=4))

    # Добавление задачи
    @classmethod
    def new_task(cls: Type["Data"], task: object) -> None:
        data = cls.load_data(cls.filename)
        data.append(task)
        for index, item in enumerate(data, start=1):
            item['id'] = index
        cls.save_data(cls.filename, data)

    @classmethod
    def add_to_treeview(cls) -> Any:
        data = cls.load_data(cls.filename)
        return data



class Logic:
    def __init__(self):
        self.task = Task
        self.data = Data()
