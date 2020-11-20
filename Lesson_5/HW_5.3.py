"""
Task 5.3
"""
with open('text_5.3.txt', 'r', encoding="utf-8") as test_file:
    user_line = test_file.readlines()
zarplata = 0
print('Сотрудники с окладом менее 20 т. рублей: ')
for x in range(len(user_line)):
    personal = user_line[x].split()
    zarplata += int(personal[1])
    if int(personal[1]) < 20000:
        print(personal[0])
print(f'Средняя величина дохода сотрудников: {zarplata/len(user_line)} рублей')
#