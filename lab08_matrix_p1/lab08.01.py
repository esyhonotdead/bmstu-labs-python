"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #8, Задание - 1, Вариант - 2
Задание: Найти строку, имеющую наибольшее количество подряд идущих одинаковых элементов.
"""

size = int(input("Введите размерность матрицы: "))
while size <= 0:
    print("Ошибка: введите положительное целое число.")
    size = int(input("Введите размерность матрицы: "))

matrix = []
for row in range(size):
    row = input("Введите элементы через пробел: ").split(" ")
    matrix.append(row)

print(f"Ваша матрица: {matrix}")

count = 0
prev_count = -1

for row in matrix:
    for el in range(1, len(row)):
        if row[el - 1] == row[el]:
            count += 1
        else:
            count = 0
    if count >= prev_count:
        prev_count = count
        row_index = matrix.index(row)

print(f"Строка с наибольшим количеством повторяющихся символов: {matrix[row_index]}")
