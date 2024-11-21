"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #9, Задание - 5
Задание:
Даны 2 матрицы А и В. Получить матрицу С, равную произведению матриц А и
В. Вывести все матрицы в виде матриц.
"""


def matrix_input(length: int) -> list:
    matrix = []
    for i in range(length):
        el = list(map(float, input(f"Введите {i + 1} строку матрицы: ").split()))
        matrix.append(el)
    return matrix


def matrix_output(matrix: list) -> None:
    for el, row in enumerate(matrix):
        string = "".join([f"{el:^10}" for el in row])
        print(f"Строка {el+1}: {string}")


def multiply_matrices(matrix_a, matrix_b: list):
    rows_matrix_a = len(matrix_a)
    cols_matrix_a = len(matrix_a[0])
    rows_matrix_b = len(matrix_b)
    cols_matrix_b = len(matrix_b[0])
    if cols_matrix_a != rows_matrix_b:
        raise ValueError(
            "Количество столбцов матрицы A должно совпадать с количеством строк матрицы B"
        )

    matrix_c = [[0] * cols_matrix_b for _ in range(rows_matrix_a)]

    for i in range(rows_matrix_a):
        for j in range(cols_matrix_b):
            for k in range(cols_matrix_a):
                matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return matrix_c


def main():
    n = int(input("Введите количество строк в матрице A: "))
    matrix_a = matrix_input(n)
    k = int(input("Введите количество строк в матрице B: "))
    matrix_b = matrix_input(k)

    matrix_c = multiply_matrices(matrix_a, matrix_b)
    print("Матрица A:")
    matrix_output(matrix_a)
    print("Матрица B:")
    matrix_output(matrix_b)
    print("Матрица C = A * B:")
    matrix_output(matrix_c)


if __name__ == "__main__":
    main()
