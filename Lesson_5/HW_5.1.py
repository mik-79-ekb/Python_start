"""
Task 5.1
"""
with open('text_5.1.txt', 'w', encoding="utf-8") as test_file:
    while True:
        user_line = f"{input('Введите новую строку: ')}"
        if user_line == '':
           break
        test_file.write(user_line + '\n')
with open('text_5.1.txt', 'r') as test_file:
    print("Содержание файла 'text_5.1.txt': ")
    print(test_file.readlines())
    #