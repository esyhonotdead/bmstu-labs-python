"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #6, Задание - 2a
Задание: Удалить элемент с заданным индексом алгоритмически
"""

import random

# задаем размер массива
while True:
    max_el = int(input("Введите число элементов в массиве: "))
    if max_el <= 0:
        print("Размер массива должен быть больше 0")
        continue
    else:
        break

# заполняем массив
my_list: list = [random.randint(-10, 10) for n in range(max_el)]
print(f"Ваш массив: {my_list}")

# значения пользователя
ind = int(input("Введите индекс элемента который надо удалить: "))

# 1 этап
for i in range(ind, len(my_list) - 1):
    my_list[i] = my_list[i + 1]

# 2 этап
my_list = my_list[:-1]

print(f"Ваш новый массив: {my_list}")
