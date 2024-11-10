"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #8, Задание - 3, Вариант - 1
Задание: Найти столбец, имеющий наибольшее количество простых чисел.
"""

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

for row in range(len(matrix)):
    for el in range(row, len(matrix)):
        matrix[row][el], matrix[el][row] = matrix[el][row], matrix[row][el]


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


max_count = -1
counter = 0

for row in matrix:
    for el in row:
        if is_prime(el):
            counter += 1
    if counter > max_count:
        max_count = counter
        max_row = matrix.index(row)

print(f"Столбец с максимальным количеством простых чисел: {max_row+1}")
