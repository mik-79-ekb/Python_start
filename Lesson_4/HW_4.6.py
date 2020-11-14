"""
Task 4.6
"""
from itertools import count, cycle
from time import sleep
first = int(input("Введите начальное число: "))
last = int(input("Введите конечное число: "))
for x in range(first, last+1):
    print(x)
    sleep(1)

n = int(input("Введите количество циклов: "))
count = 1
a = ["Рассказать тебе", "сказку про", "белого бычка?"]
for x in cycle(a):
    if count > (n * len(a)):
        break
    print(x)
    sleep(1)
    count += 1