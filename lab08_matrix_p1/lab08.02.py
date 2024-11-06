"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #8, Задание - 2
Задание: Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов.
"""

import math

size = int(input("Введите размерность матрицы: "))
while size <= 0:
    print("Ошибка: введите положительное целое число.")
    size = int(input("Введите размерность матрицы: "))

matrix = []
for row in range(size):
    row = input("Введите элементы через пробел: ").split(" ")
    for i in range(len(row)):
        row[i] = float(row[i])
    matrix.append(row)

print(f"Ваша матрица: {matrix}")

min_count = math.inf
max_count = -1

counter = 0
el = 0
for row in matrix:
    while el > len(row):
        if row[el - 1] < 0:
            counter += 1
        el += 1
    if counter > max_count:
        max_count = counter
        index_max = matrix.index(row)
    if counter < min_count:
        min_count = counter
        index_min = matrix.index(row)

matrix[index_max], matrix[index_min] = matrix[index_min], matrix[index_max]

print(f"Изменённая матрица: {matrix}")
