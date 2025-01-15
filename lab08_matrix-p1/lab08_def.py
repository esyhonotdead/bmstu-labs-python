"""
Дана квадратная целочисленная матрица найти минимальный элемент на побочной диагонали
Поменять местами строку и столбец
Замену произвести в исходной матрице новую матрицу не создавать
"""

matrix = [
    [2, 5, 8, 9, 7],
    [1, 9, 2, 3, 1],
    [7, -1, 1, 1, 0],
    [8, -1, 1, 7, 5],
    [0, 0, 0, 0, 0],
]


for row in matrix:
    print(row)
print("")

size = len(matrix)
min_el = 10**8
min_ind = 0

for i in range(size):
    for j in range(size):
        if i == size - 1 - j:
            if matrix[i][j] <= min_el:
                min_el = matrix[i][j]
                min_ind = (i, j)

for i in range(size):
    matrix[i][min_ind[1]], matrix[min_ind[0]][size - i - 1] = (
        matrix[min_ind[0]][size - i - 1],
        matrix[i][min_ind[1]],
    )


for row in matrix:
    print(row)
