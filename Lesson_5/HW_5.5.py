"""
Task 5.5
"""
with open('text_5.5.txt', 'w', encoding="utf-8") as test_file:
    user_numbers = f"{input('Введите набор чисел через пробел: ')}"
    test_file.write(user_numbers)
with open('text_5.5.txt', 'r', encoding="utf-8") as test_file:
    numbers = user_numbers.split()
    sum_numbers = 0
    for x in range(len(numbers)):
        sum_numbers += int(numbers[x])
print(f'Сумма введенных чисел составила: {sum_numbers}')