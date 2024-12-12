"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #13
Задание:
База данных в файле
"""

from dataclasses import dataclass

"""
1) Создать структуру
2) Записать в базу данных
"""


@dataclass
class User:
    name: str
    age: int
    work: str


igor = User("Igor", "23", "Dolbaeb")

print(igor.name, type(igor.age), igor.work)
