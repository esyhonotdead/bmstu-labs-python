"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #6, Задание - 1a
Задание: Добавить элемент в заданное место списка (по индексу) с использованием любых средств Python.
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
i = int(input("Введите индекс: "))

# добовляем элемент в массив
my_list.insert(i, num)

print(f"Ваш новый массив: {my_list}")