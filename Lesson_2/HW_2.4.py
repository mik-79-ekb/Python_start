"""
Task 2.4
"""
stroka = input("Введите строку: ").split()
ind = 1
for x in stroka:
    print(f"{ind}: {x[:10]}")
    ind += 1