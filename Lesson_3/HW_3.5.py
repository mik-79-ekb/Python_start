"""
Task 3.5
"""
def num_summa ():
    summa = 0
    while True:
        chisla = input("Введите строку чисел и '+' для остановки: ")
        if '+' in chisla:
            chisla = chisla.replace('+', "")
            summa += sum(map(int, chisla.split()))
            break
        summa += sum(map(int, chisla.split()))
        print(f"Сумма уже введенных чисел: {summa}")
    return summa
print(f"Общая сумма чисел: {num_summa()}")