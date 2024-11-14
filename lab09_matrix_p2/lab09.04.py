"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #9, Задание - 4
Задание:
Задана матрица D и массив I, содержащий номера строк, для которых
необходимо определить максимальный элемент. Значения максимальных
элементов запомнить в массиве R. Определить среднее арифметическое
вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
среднее арифметическое значение.
"""


def matrix_input(lenght: int) -> list:
    matrix = []
    for i in range(lenght):
        el = list(map(float, input(f"Введите {i + 1} строку матрицы: ").split()))
        matrix.append(el)
    return matrix


def matrix_output(matrix: list) -> None:
    for el, row in enumerate(matrix):
        string = "".join([f"{el:^10}" for el in row])
        print(f"Строка {el+1}: {string}")


def max_in_row(matrix: list, row_i: list) -> list:
    row_r = []
    for i in row_i:
        if i in range(len(matrix)):
            row_r.append(max(matrix[i]))
    return row_r


def row_average(row: list) -> int:
    return lambda i, n: sum(i) / len(n)


def main():
    n = int(input("Введите количество строк в матрице: "))
    matrix = matrix_input(n)
    row_i = map(int, input("Введите номера строк: ").split(" "))
    max_nums = max_in_row(matrix, row_i)
    matrix_output(matrix)
    print(f"Строки поиска: {[row_i]}")
    print(f"Максимальные элементы в строках: {max_nums}")
    print(f"Среднеее арифметическое значение: {row_average(max_nums)}")


if __name__ == "__main__":
    main()
