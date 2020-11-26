"""
Task 5.6
"""
lessons_dict = {}
with open('text_5.6.txt', 'r', encoding="utf-8") as test_file:
    user_list = test_file.readlines()
    for x in range(len(user_list)):
        lessons = user_list[x].split(':')
        user_string = ''.join(lessons)
        user_string = user_string.replace('(', ' ')
        lesson = str(user_string)
        lesson = lesson.split(' ')
        nagruzka = 0
        for x in lesson:
            try:
                value = int(x)
                nagruzka += value
            except:
                pass
        lessons_dict[lessons[0]] = nagruzka
print(lessons_dict)
#