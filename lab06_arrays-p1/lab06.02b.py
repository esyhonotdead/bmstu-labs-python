"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #6, Задание - 2b
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
arr: list = [random.randint(-10, 10) for n in range(max_el)]
print(f"Ваш массив: {arr}")

# значения пользователя
ind = int(input("Введите индекс элемента который надо удалить: "))

# 1 этап
for i in range(ind, len(arr) - 1):
    arr[i] = arr[i + 1]

# 2 этап
arr = arr[:-1]

print(f"Ваш новый массив: {arr}")
