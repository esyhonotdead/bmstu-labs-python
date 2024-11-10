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
    """Ввод квадратной матрицы"""
    matrix = []
    for i in range(lenght):
        el = list(map(int, input(f"Введите {i + 1} строку матрицы: ").split()))
        matrix.append(el)
    return matrix


def matrix_output(matrix: list) -> None:
    """Вывод матрицы"""
    output_string = ""
    for i, string in enumerate(matrix):
        output = "".join([f"{s:^6.6g}" for s in string])
        output_string += f"Строка {i + 1} = {output}\n"
    print(output_string)


def rotate_right(matrix: list):
    return tuple(zip(*matrix[::-1]))


def rotate_left(matrix: list):
    return tuple(zip(*matrix))[::-1]


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
