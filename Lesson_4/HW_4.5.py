"""
Task 4.5
"""
from functools import reduce
product_all = reduce(lambda x, y: x * y, [x for x in range(100, 1001) if x % 2 == 0])
print(f"Произведение четных чисел от 100 до 1000 равно: {product_all}")