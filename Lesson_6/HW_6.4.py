"""
Task 6.4
"""
class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = str
        self.speed = speed
        self.color = str
        self.is_police = is_police

    def go (self):
        return print(f'Машина поехала')
    def stop (self):
        return print(f'Машина остановилась')
    def turn (self, direction):
        return print(f'Машина повернула {direction}')
    def show_speed(self):
        return print(f'Ваша скорость: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print(f'!!!Ваша скорость Превышена!!!: {self.speed}')
        else:
            return print(f'Ваша скорость: {self.speed}')
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print(f'!!!Ваша скорость Превышена!!!: {self.speed}')
        else:
            return print(f'Ваша скорость: {self.speed}')
class PoliceCar(Car):
    pass

town = TownCar('Ford', 80, 'серый', False)
print('TownCar')
town.go()
town.show_speed()
town.turn('налево')
town.turn('налево')
town.stop()

sport = SportCar('BMW', 140, 'желтый', False)
print('SportCar')
sport.go()
sport.show_speed()
sport.turn('направо')
sport.turn('налево')
sport.turn('направо')
sport.stop()

work = WorkCar('KAMAZ', 35, 'оранжевый', False)
print('WorkCar')
work.go()
work.show_speed()
work.turn('направо')
work.turn('налево')
work.stop()

police = PoliceCar('Jaguar', 120, 'белый', True)
print('PoliceCar')
police.go()
police.show_speed()
police.turn('налево')
police.turn('налево')
police.turn('налево')
police.turn('налево')
police.stop()