"""
Task 6.5
"""
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw (self):
        return print(f'Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        return print(f'Вы рисуете {self.title}!')
class Pencil(Stationery):
    def draw(self):
        return print(f'Вы рисуете {self.title}!')
class Handle(Stationery):
    def draw(self):
        return print(f'Вы рисуете {self.title}!')

p = Pen('ручкой')
pl = Pencil('карандашем')
h = Handle('маркером')
p.draw()
pl.draw()
h.draw()