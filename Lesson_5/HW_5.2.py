"""
Task 5.2
"""
with open('text_5.2.txt', 'r', encoding="utf-8") as test_file:
    user_line = test_file.readlines()
print(f'Общее количество строк в файле: {len(user_line)}')
for x in range(len(user_line)):
    slova = user_line[x].split()
    print(f'В {x+1} строке файла {len(slova)} слов')
#