"""
Task 4.1
"""
from sys import argv
def raschet (virabotka, stavka, premiya):
    return int(virabotka) * int(stavka) + int(premiya)
_, virabotka, stavka, premiya = argv
print(f"Результат: {raschet(virabotka, stavka, premiya)}")
