"""
Task 6.1
"""
from time import sleep

class TrafficLight:
    __color = 'Красный'

    def running (self):
        print(f"Начало работы светофора!")
        self.__color ='Красный'
        print(f'Цвет светофора: {self.__color}')
        sleep(7)
        self.__color ='Желтый'
        print(f'Цвет светофора: {self.__color}')
        sleep(2)
        self.__color ='Зеленый'
        print(f'Цвет светофора: {self.__color}')
        sleep(5)

t_light = TrafficLight()
t_light.running()