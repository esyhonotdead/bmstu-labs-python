"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #9, Задание - 2
Задание:
Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
стрелке, затем на 90 градусов против часовой стрелки.
Вывести исходную, промежуточную и итоговую матрицы.
Дополнительных матриц и массивов не вводить. Транспонирование не применять.
"""


def matrix_input(lenght: int) -> list:
    matrix = []
    for i in range(lenght):
        el = list(map(int, input(f"Введите {i + 1} строку матрицы: ").split()))
        matrix.append(el)
    return matrix


def matrix_output(matrix: list) -> None:
    for el, row in enumerate(matrix):
        string = "".join([f"{el:^10}" for el in row])
        print(f"Строка {el+1}: {string}")


def rotate_left(matrix):
    rotated_matrix = [list(row) for row in zip(*matrix)][::-1]
    return rotated_matrix


def rotate_right(matrix):
    rotated_matrix = [list(row)[::-1] for row in zip(*matrix)]
    return rotated_matrix


def main():
    n = int(input("Введите размер квадратной матрицы: "))
    matrix = matrix_input(n)

    print("Исходная матрица")
    matrix_output(matrix)

    matrix = rotate_right(matrix)
    print("Промежуточная матрица")
    matrix_output(matrix)

    matrix = rotate_left(matrix)
    print("Итоговая матрица")
    matrix_output(matrix)


if __name__ == "__main__":
    main()
