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

print("\n Введенная матрица: ")
for i, lenght in enumerate(matrix):
    string = "".join([f"{e:^10}" for e in lenght])
    print(f"matrix[{i}] = {string}")


min_count = math.inf
max_count = -1

counter = 0
el = 0

for row in range(len(matrix)):
    for el in matrix[row]:
        if el >= 0:
            counter += 1
    if counter > max_count:
        max_count = counter
        index_max = row
    if counter < min_count:
        min_count = counter
        index_min = row

matrix[index_max], matrix[index_min] = matrix[index_min], matrix[index_max]

print("\n Измененная матрица: ")
for i, lenght in enumerate(matrix):
    string = "".join([f"{e:^10}" for e in lenght])
    print(f"matrix[{i}] = {string}")
