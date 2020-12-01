"""
Task 8.1
"""
import datetime

class Data:
    def __init__(self, data):
        self.data = data.split('-')
        print(self.data)

    @classmethod
    def chislo(cls, data):
        data = data.split('-')
        for x in data:
            x = int(x)
            print(f'Значение: {x}, тип: {type(x)}')
        return data

    @staticmethod
    def validation(data):
        try:
            datetime.datetime.strptime(data, '%d-%m-%Y')
            return print('Правильный формат даты!')
        except ValueError: print('Неправильная дата / формат даты, надо ДД-ММ-ГГГГ!')

d = Data('19-03-2020')
Data.chislo('19-03-2020')
Data.validation('19-03-2020')
Data.validation('19-13-2020')