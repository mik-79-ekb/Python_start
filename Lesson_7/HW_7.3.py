"""
Task 7.3
"""
class Kletka:
    def __init__(self, index):
        self.index = int(index)

    def __add__(self, other):
        return f'Клетка увеличилась, ее размер стал: {self.index + other.index}'
    def __sub__(self, other):
        return f'Клетка уменьшилась, ее размер стал: {self.index - other.index}' if self.index - other.index > 0 else f'Уменьшение клетки невозможно!'
    def __mul__(self, other):
        return f'Клетка разрослась, ее размер стал: {self.index * other.index}'
    def __truediv__(self, other):
        return f'Клетка разделилась, ее размер стал: {self.index // other.index}'
    def make_order(self, row):
        result = ''
        for i in range(int(self.index / row)):
            result += '*' * row + '\n'
        result += '*' * (self.index % row) + '\n'
        return result

k_1 = Kletka(12)
k_2 = Kletka(5)
print(k_1.__add__(k_2))
print(k_1.__sub__(k_2))
print(k_1.__mul__(k_2))
print(k_1.__truediv__(k_2))
print(f'Разбиение клетки k_1:')
print(k_1.make_order(5))
print(f'Разбиение клетки k_2:')
print(k_2.make_order(5))