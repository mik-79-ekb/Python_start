"""
Task 8.3
"""
class NumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

result = []
def numberlist():
    while True:
        user_list = input('Введите число или >stop< для остановки: ')
        if user_list == 'stop':
            print(f'Введенный набор чисел: {result}')
            break
        try:
            if not user_list.isnumeric():
                raise NumberError('Упс!')
            result.append(int(user_list))
        except NumberError as error:
            print('Внимательнееб это не число!')
numberlist()