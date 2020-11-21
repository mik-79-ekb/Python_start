"""
Task 4.6
"""
from itertools import count, cycle
from time import sleep
first = int(input("Введите начальное число: "))
last = int(input("Введите конечное число: "))
i = 1
for x in count(first):
    if i > (last-first+1):
        break
    print(x)
    sleep(1)
    i += 1

n = int(input("Введите количество циклов: "))
i = 1
a = ["Рассказать тебе", "сказку про", "белого бычка?"]
for x in cycle(a):
    if i > (n * len(a)):
        break
    print(x)
    sleep(1)
    i += 1