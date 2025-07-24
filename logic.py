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

