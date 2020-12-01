"""
Task 8.2
"""
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

def delO():
    try:
        chislitel = int(input('Введите числитель дроби: '))
        znamenatel = int(input('Введите знаменатель дроби: '))
        if znamenatel == 0:
            raise OwnError("На ноль делить нельзя, помните об этом!")
    except ValueError:
        print("Вы ввели не число! Будьте внимательней.")
    except OwnError as err:
        print(err)
    else:
        print(f"Вы молодец! Ваш результат: {chislitel / znamenatel}")

delO()