"""
Task 3.1
"""
def div(*args):
    try:
        return d1 / d2
    except ZeroDivisionError:
        print("На 0 делить нельзя!")
d1 = int(input("Введите первое число: "))
d2 = int(input("Введите второе число: "))
print(f"Результат от деления {d1} на {d2} равен: {div(d1,d2)}")