"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #8, Задание - 5
Задание: Найти максимальное значение в квадратной матрице над главной диагональю и минимальное - под побочной диагональю.
"""

size = int(input("Введите размерность матрицы: "))
while size <= 0:
    print("Ошибка: введите положительное целое число.")
    size = int(input("Введите размерность матрицы: "))


matrix = []
for row in range(size):
    row = input("Введите элементы через пробел: ").split(" ")
    for row in range(len(row)):
        row[row] = float(row[row])
    matrix.append(row)

max_num = 0
min_num = 10**-8

for row in range(size):
    for el in range(row):
        max_num = max(max_num, matrix[el][row])

for x in range(len(matrix[0])):
    for y in range(size - x, size):
        min_num = min(min_num, matrix[y][x])

print(f"Минимальный элемент: {min_num}")
print(f"Максимальный элемент: {max_num}")
