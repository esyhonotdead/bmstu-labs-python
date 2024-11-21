"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #9, Задание - 2
Задание:
Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
стрелке, затем на 90 градусов против часовой стрелки.
Вывести исходную, промежуточную и итоговую матрицы.
Дополнительных матриц и массивов не вводить. Транспонирование не применять.
"""


def matrix_input(length: int) -> list:
    matrix = []
    for i in range(length):
        el = list(map(int, input(f"Введите {i + 1} строку матрицы: ").split()))
        matrix.append(el)
    return matrix


def matrix_output(matrix: list) -> None:
    for el, row in enumerate(matrix):
        string = "".join([f"{el:^10}" for el in row])
        print(f"Строка {el+1}: {string}")


def rotate_left(matrix: list, n: int) -> list:
    rotated_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_matrix[n - j - 1][i] = matrix[i][j]
    return rotated_matrix


def rotate_right(matrix: list, n: int) -> list:
    rotated_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n - i - 1] = matrix[i][j]
    return rotated_matrix


def main():
    n = int(input("Введите размер квадратной матрицы: "))
    matrix = matrix_input(n)

    print("Исходная матрица")
    matrix_output(matrix)

    matrix = rotate_right(matrix, n)
    print("Промежуточная матрица")
    matrix_output(matrix)

    matrix = rotate_left(matrix, n)
    print("Итоговая матрица")
    matrix_output(matrix)


if __name__ == "__main__":
    main()
