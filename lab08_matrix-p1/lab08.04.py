"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #8, Задание - 4
Задание: Переставить местами столбцы с максимальной и минимальной суммой элементов.
"""

size = int(input("Введите количество строк: "))
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

max_sum = 0
min_sum = 10**6
index_max = 0
index_min = 0


for i in range(size):
    row_sum = 0
    for el in range(size):
        row_sum += matrix[el][i]

    if row_sum > max_sum:
        index_max = i
        max_sum = row_sum

    if row_sum < min_sum:
        index_min = i
        min_sum = row_sum

for i in range(size):
    matrix[i][index_max], matrix[i][index_min] = (
        matrix[i][index_min],
        matrix[i][index_max],
    )

print("\n Измененная матрица: ")
for i, lenght in enumerate(matrix):
    string = "".join([f"{e:^10}" for e in lenght])
    print(f"matrix[{i}] = {string}")
