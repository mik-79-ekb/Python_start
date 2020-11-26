"""
Task 5.4
"""
lang_dict = {'One': 'Один','Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('start_5.4.txt', 'r', encoding="utf-8") as start_file:
    with open('finish_5.4.txt', 'w', encoding="utf-8") as finish_file:
        user_line = start_file.readlines()
        for x in range(len(user_line)):
            line = user_line[x].split()
            finish_file.write(f"{lang_dict[line[0]]} {line[1]} {line[2]}\n")
            #