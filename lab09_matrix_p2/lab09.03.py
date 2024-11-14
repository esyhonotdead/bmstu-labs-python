"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #9, Задание - 3
Задание:
Даны две матрицы A и B, в которых количество столбцов одинаково.
Подсчитать для каждого столбца матрицы А количество элементов, больших
среднего арифметического элементов соответствующего столбца матрицы В.
Вывести полученные значения. Затем преобразовать матрицу В путем
умножения всех элементов столбца матрицы на посчитанное для этого столбца
значение, если оно ненулевое. Вывести преобразованную матрицу в виде
матрицы
"""


def matrix_input(lenght: int) -> list:
    matrix = []
    for i in range(lenght):
        el = list(map(float, input(f"Введите {i + 1} строку матрицы: ").split()))
        matrix.append(el)
    return matrix


def rotate_left(matrix):
    rotated_matrix = [list(row) for row in zip(*matrix)][::-1]
    return rotated_matrix


def rotate_right(matrix):
    rotated_matrix = [list(row)[::-1] for row in zip(*matrix)]
    return rotated_matrix


def average_coloumn(matrix: list) -> list[list[int]]:
    coloumn_average = []
    for row in matrix:
        row_sum = sum(row)
        el_num = len(row)
        average = row_sum / el_num
        coloumn_average.append(average)
    return coloumn_average


def greater_nums_in_row(matrix: list, averages: list) -> list[list[int]]:
    greater_rows = []
    counter = 0
    for row_ind, row in enumerate(matrix):
        for el in row:
            if el > averages[row_ind]:
                counter += 1
        greater_rows.append(counter)
        counter = 0
    return greater_rows


def multiply_matrix(matrix: list, multipliers: list) -> list[list[int]]:
    for i in range(len(matrix)):
        if multipliers[i] != 0:
            matrix[i] = [element * multipliers[i] for element in matrix[i]]
    return matrix


def matrix_output(matrix: list) -> None:
    for el, row in enumerate(matrix):
        string = "".join([f"{el:^10}" for el in row])
        print(f"Строка {el+1}: {string}")


def main():
    n = int(input("Введите количество строк в матрице: "))
    print("Матрица A.")
    matrix_a = matrix_input(n)
    print("Матрица B.")
    matrix_b = matrix_input(n)
    averages = average_coloumn(rotate_right(matrix_b))
    greater_rows = greater_nums_in_row(rotate_right(matrix_a), averages)
    b_rotated = rotate_right(matrix_b)
    edited_b = multiply_matrix(b_rotated, greater_rows)
    print("Ответ: ")
    matrix_output(rotate_left(edited_b))


if __name__ == "__main__":
    main()
