"""
Task 4.7
"""
def factorial(chislo):
    ind = 1
    for x in range(1, chislo + 1):
        ind *= x
        yield ind
chislo = int(input("Введите факториалы n! до какого числа Вы хотите узнать: "))
for x in factorial(chislo):
    print(x)