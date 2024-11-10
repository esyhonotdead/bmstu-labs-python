"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #8, Задание - 6
Задание: Выполнить транспонирование квадратной матрицы.
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


for row in range(len(matrix)):
    for el in range(row, len(matrix)):
        matrix[row][el], matrix[el][row] = matrix[el][row], matrix[row][el]

print("\n Измененная матрциа: ")
for i, lenght in enumerate(matrix):
    string = "".join([f"{e:^10}" for e in lenght])
    print(f"matrix[{i}] = {string}")
