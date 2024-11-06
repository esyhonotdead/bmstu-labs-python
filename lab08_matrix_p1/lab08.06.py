"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #8, Задание - 6
Задание: Выполнить транспонирование квадратной матрицы.
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

for row in range(len(matrix)):
    for el in range(row, len(matrix)):
        matrix[row][el], matrix[el][row] = matrix[el][row], matrix[row][el]

print(f"Транспонированная матрица {matrix}")
