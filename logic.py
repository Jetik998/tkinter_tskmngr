import json

class Task:
    def __init__(self, name=None, priority=None,deadline=None):
        self.name = name
        self.priority = priority
        self.deadline = deadline
    def __str__(self):
        return f'{self.name} {self.priority} {self.deadline}'
    def __repr__(self):
        return f'{self.name} {self.priority} {self.deadline}'

class Data:
    data = []

    @classmethod
    def add_task(cls, name, priority, deadline):
        task = Task(name=name, priority=priority, deadline=deadline)
        cls.data.append(task)
        print(cls.data)

    @classmethod
    def add_json(cls):
        with open(json_data, 'w', encoding='utf-8') as file:
            json.dump(cls.data, file, ensure_ascii=False, indent=4)

class Logic:
    def __init__(self):
        self.task = []
        self.data = Data()
