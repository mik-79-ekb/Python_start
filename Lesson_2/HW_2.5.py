"""
Task 2.5
"""
list = [7, 5, 3, 3, 2]
rating = int(input("Введите новый рейтинг: "))
ind= 0
for x in list:
    if rating <= x:
        ind += 1
list.insert(ind, rating)
print(list)