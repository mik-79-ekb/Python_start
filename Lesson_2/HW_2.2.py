"""
Task 2.2
"""
list = list(input("Введите список: "))
for x in range(1, len(list), 2):
    list[x - 1], list[x] = list[x], list[x - 1]
print(f"Измененный список: {list}")