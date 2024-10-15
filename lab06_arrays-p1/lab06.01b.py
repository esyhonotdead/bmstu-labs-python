"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #6, Задание - 1b
Задание: Добавить элемент в заданное место списка (по индексу) алгоритмически.
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
num = int(input("Введите число: "))
ind = int(input("Введите индекс: "))

# 1 этап
my_list.append(None)

# 2 этап
for i in range(len(my_list) - 2, ind - 1, -1):
    my_list[i + 1] = my_list[i]

# 3 этап
my_list[i] = num

print(f"Ваш новый массив: {my_list}")
