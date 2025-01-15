"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #9, Задание - 7
Задание:
Ввести трёхмерный массив (массив матриц размера X*Y*Z). Вывести срез
массива по большему измерению, индекс среза – середина размерности с
округлением в меньшую сторону.
"""


def main():
    square_matrix = []
    z = int(input("Введите Z: "))
    while z < 1:
        z = int(input("Введите Z: "))
    y = int(input("Введите Y: количество строк в матрице "))
    while y < 1:
        y = int(input("Введите Y: "))

    for z_i in range(z):
        matrix = []
        for y_i in range(y):
            line = [
                int(i)
                for i in input(f"Введите {y_i + 1} строку {z_i + 1} матрицы ")
                .strip()
                .split()
            ]

            matrix.append(line)
        square_matrix.append(matrix)

    x = len(square_matrix[0][0])
    if x > y:
        if x > z:
            middle = (x - 1) // 2
            print(
                *[[matrix[i][middle] for matrix in square_matrix] for i in range(y)],
                sep="\n",
            )
        else:
            middle = (z - 1) // 2
            print(*square_matrix[middle], sep="\n")
    elif z > y:
        middle = (z - 1) // 2
        print(*square_matrix[middle], sep="\n")
    else:
        middle = (y - 1) // 2
        print(*[matrix[middle] for matrix in square_matrix], sep="\n")


if __name__ == "__main__":
    main()
