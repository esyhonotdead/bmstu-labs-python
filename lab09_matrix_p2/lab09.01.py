"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #9, Задание - 1
Задание:
Даны два одномерных целочисленных массива A и B. Сформировать матрицу M, такую что m(ij)=a(i)*j(j).
Определить количество полных квадратов в каждой строке матрицы.
Записать значения в массив S.
Напечатать матрицу M в виде матрицы и рядом столбец S.
"""

from math import sqrt


def list_input(length: int) -> list:
    temp_list = []
    for i in range(length):
        el = int(input(f"Введите {i+1} элемент массива: "))
        temp_list.append(el)
    return temp_list


def create_matrix(a, b: list, lenght: int) -> list:
    matrix = [[0] * lenght for i in range(lenght)]
    for i in range(lenght):
        for j in range(lenght):
            matrix[i][j] = a[i] * b[j]
    return matrix


def count_squares(matrix: list, counter: int) -> list:
    full_squares = []
    for row in matrix:
        for el in row:
            el = sqrt(el)
            if el == int(el):
                counter += 1
        row_count = counter
        counter = 0
        full_squares.append(row_count)
    return full_squares


def matrix_output(matrix, n: list) -> None:
    print("Ответ:")
    for el, row in enumerate(matrix):
        string = "".join([f"{el:^10}" for el in row])
        print(f"Строка {el+1}: {string} количество полных квадратов: {n[el]}")


def main():
    counter = 0
    n = int(input("Введите количество элементов в списках: "))
    print("Введите массив A.")
    list_a = list_input(length=n)
    print("Введите массив B.")
    list_b = list_input(length=n)
    matrix = create_matrix(list_a, list_b, n)
    matrix_squares = count_squares(matrix, counter)
    matrix_output(matrix, matrix_squares)


if __name__ == "__main__":
    main()
