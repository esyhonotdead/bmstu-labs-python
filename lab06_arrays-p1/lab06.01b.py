"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #6, Задание - 1b
Задание: Добавить элемент в заданное место списка (по индексу) алгоритмически.
"""

import numpy as np

# задаем размер массива
while True:
    max_el = int(input("Введите число элементов в массиве: "))
    if max_el <= 0:
        print("Размер массива должен быть больше 0")
        continue
    else:
        break

# заполняем массив
arr: list = np.random.randint(-10, 10, size=20)
print(f"Ваш массив: {arr}")

# значения пользователя
num = int(input("Введите число: "))
ind = int(input("Введите индекс: "))

# 1 этап
arr.append(None)

# 2 этап
for i in range(len(arr) - 2, ind - 1, -1):
    arr[i + 1] = arr[i]

# 3 этап
arr[i] = num

print(f"Ваш новый массив: {arr}")
