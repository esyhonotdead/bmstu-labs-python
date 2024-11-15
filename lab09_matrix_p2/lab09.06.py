"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #9, Задание - 6
Задание:
Дана матрица символов. Преобразовать её следующим образом: заменить все
согласные латинские букв на заглавные, а все гласные латинские буквы на
строчные. Вывести матрицу до преобразования и после
"""


def matrix_input(lenght: int) -> list:
    matrix = []
    for i in range(lenght):
        el = list(map(str, input(f"Введите {i + 1} строку матрицы: ").split()))
        matrix.append(el)
    return matrix


def matrix_output(matrix: list) -> None:
    for el, row in enumerate(matrix):
        string = "".join([f"{el:^10}" for el in row])
        print(f"Строка {el+1}: {string}")


def matrix_edit(matrix: list) -> list:
    vowels = ("A", "E", "U", "I", "O", "Y")
    a_uni = 65
    z_uni = 90

    for line in matrix:
        for index in range(len(line)):
            if a_uni <= ord(line[index].upper()) <= z_uni:
                if line[index].upper() in vowels:
                    line[index] = line[index].lower()
                else:
                    line[index] = line[index].upper()
    return matrix


def main():
    n = int(input("Введите количество строк в матрице: "))
    matrix = matrix_input(n)
    print("Введенная матрица: ")
    matrix_output(matrix)
    print("Измененная матрица: ")
    matrix_output(matrix_edit(matrix))


if __name__ == "__main__":
    main()
