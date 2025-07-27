import json
from typing import Type
from typing import List



class Task:
    def __init__(self, name=None, priority=None,deadline=None):
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

class Data:
    data = []

    # Добавить задачу(объект) в список
    @classmethod
    def add_list(cls: Type["Data"], task) -> None:
        cls.data.append(task)
        print(cls.data)

    # Присвоение id
    @classmethod
    def generate_ids(cls: Type["Data"]) -> None:
        for i, task in enumerate(cls.data, start=1):
            task.id = i

    #Сериализация
    @classmethod
    def to_dict(cls: Type["Data"]) -> List[dict]:
        return [task.__dict__ for task in cls.data]

    @classmethod
    def add_json(cls: Type["Data"]):
        with open("data.json", 'w', encoding='utf-8') as file:
            json.dump(cls.to_dict(), file, ensure_ascii=False, indent=4)

    @staticmethod
    def view_json() -> None:
        with open("data.json", 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)

    #Оркестратор
    @classmethod
    def new_task(cls: Type["Data"], task: object) -> None:
        cls.add_list(task)
        cls.generate_ids()
        cls.to_dict()
        cls.add_json()
        cls.view_json()





class Logic:
    def __init__(self):
        self.task = Task
        self.data = Data()
