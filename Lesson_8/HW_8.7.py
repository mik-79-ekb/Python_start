"""
Task 8.7
"""
class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма чисел равна: ')
        return f'{self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение чисел равно: ')
        return f'{self.a * other.a - (self.b * other.b)} + {self.a * other.b + other.a * self.b} * i'

n_1 = ComplexNumber(5, 8)
n_2 = ComplexNumber(-1, 2)
print(n_1.__add__(n_2))
print(n_1.__mul__(n_2))