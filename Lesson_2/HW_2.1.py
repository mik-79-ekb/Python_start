"""
Task 2.1
"""
list = [1, 1.0, True, 'stroka', complex (2, 4), None, [1, 2], (1, 2), {1, 2}, {1:1, 2:2}]
for elem in list:
    print(f"Данные вида {elem} имеют тип: {type(elem)})")