"""
Task 3.2
"""
def person (**kwargs):
    return (" ".join(map(str, list(kwargs.values()))))
print(person(name="Иван", surname="Иванов", bith_year="2000", city="Ивановск", email="ivanov@mail.com", phone="+7-000-000-00-00"))