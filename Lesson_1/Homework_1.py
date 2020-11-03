#1
print ("Part 1.1")
a = 1
b = 1.1
c = False
d = 'hello python'
f_a = f" Для данных '{a}' - тип '{type(a)}'"
print(f_a)
f_b = f" Для данных '{b}' - тип '{type(b)}'"
print(f_b)
f_c = f" Для данных '{c}' - тип '{type(c)}'"
print(f_c)
f_d = f" Для данных '{d}' - тип '{type(d)}'"
print(f_d)

print ()
print ("Part 1.2")
chislo = input(" Пожалуйста введите число: ")
chislo = int(chislo)
f_chislo = f"'{chislo}' - тип '{type(chislo)}'"
print(f_chislo)
stroka = input(" Пожалуйста введите текст: ")
f_stroka = f"'{stroka}' - тип '{type(stroka)}'"
print(f_stroka)

#2
print ()
print ("Part 2.0")
usernum = input(" Пожалуйста введите количество секунд: ")
usernum = int(usernum)
u_hour = usernum // (60 * 60)
u_min = (usernum - u_hour * (60 * 60)) // 60
u_sec = usernum - u_hour * (60 * 60) - u_min * 60
result = f"Вы ввели следующее время: {u_hour:02}:{u_min:02}:{u_sec:02}"
print(result)

#3
print ()
print ("Part 3.0")
user_num = input(" Пожалуйста введите число: ")
user_num = f"{int(user_num) + int(user_num*2) + int(user_num*3)}"
print(f"Ответ: {user_num}")

#4
print ()
print ("Part 4.0")
us_number = input("Пожалуйста введите число: ")
us_number = int(us_number)
max_un = us_number % 10
us_number = us_number // 10
while us_number >= 1:
    if max_un < us_number % 10:
       max_un = us_number % 10
    us_number = us_number // 10
print(f"Максимальная цифра числа: {max_un}")

#5
print ()
print ("Part 5.0")
reverue = input("Пожалуйста введите размер выручки: ")
reverue = int(reverue)
costs = input("Пожалуйста введите размер затрат: ")
costs = int(costs)
if reverue > costs:
    print("Ваш финансовый результат - прибыль!")
    print(f"Размер прибыли составил: {reverue - costs}")
    print(f"Валовая рентабельность: {round(((reverue - costs) / reverue * 100), 1)} %")
    staff = input("Пожалуйста введите количество сотрудников: ")
    staff = int(staff)
    print(f"Доход на 1 сотрудника составил: {round(((reverue - costs) / staff), 1)}")
elif reverue == costs:
    print("Ваш финансовый результат - ноль!")
else: print("Ваш финансовый результат - убыток!")

#6
print ()
print ("Part 6.0")
start = input("Пожалуйста введите начальный результат: ")
start = int(start)
finish = input("Пожалуйста введите конечный результат: ")
finish= int(finish)
day = 0
while start <= finish:
    start = start * 1.1
    day += 1
print(f"Ответ: на {day} день спортсмен достиг результата — не менее {finish} км.")