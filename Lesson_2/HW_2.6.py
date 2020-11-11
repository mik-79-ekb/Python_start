"""
Task 2.6
"""
structura = {"Название": "", "Цена": "", "Количество": "", "Единица измерения": ""}
analitica = {"Название": [], "Цена": [], "Количество": [], "Единица измерения": []}
sklad = []
ind = 1
while True:
    if input("Для выхода нажмите -->+<--, для продолжения -->Enter<--:") == "+":
        break
    for key in structura:
        s = input(f"Введите характеристику >{key}<: ")
        structura[key] = s
    sklad.append((ind, structura.copy()))
    ind += 1
print(sklad)
for number, dict in sklad:
    for key, value in dict.items():
        analitica[key].append(value)
print(analitica)