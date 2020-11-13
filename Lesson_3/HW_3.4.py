"""
Task 3.4
"""
def my_func1 (x, y):
        return (x ** y)
def my_func2 (x, y):
        i = 1
        var = 1
        while i <= abs(y):
                var = var * 1 / x
                i += 1
        return var
print(f" Первый вариант: {my_func1(3, -7)}")
print(f" Второй вариант: {my_func2(3, -7)}")
print(f" Проверка (встроенная функция): {pow(3, -7)}")