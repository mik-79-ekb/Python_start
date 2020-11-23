"""
Task 6.3
"""
class Worker:
    name = None
    surname = None
    position = None
    _income = {'wage': [], 'bonus': []}

class Position(Worker):
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income

    def get_full_name (self):
        return f'{self.name} {self.surname}'
    def get_total_income (self):
        return self._income['wage'] + self._income['bonus']

position = Position('Иван', 'Иванов', 'Специалист', {'wage': 50000, 'bonus': 25000})
print(position.get_full_name())
print(position.get_total_income())