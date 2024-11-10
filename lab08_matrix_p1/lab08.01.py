"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #8, Задание - 1, Вариант - 2
Задание: Найти строку, имеющую наибольшее количество подряд идущих одинаковых элементов.
"""

size = int(input("Введите количество строк: "))
while size <= 0:
    print("Ошибка: введите положительное целое число.")
    size = int(input("Введите размерность матрицы: "))

matrix = []
for row in range(size):
    row = input("Введите элементы через пробел: ").split(" ")
    matrix.append(row)

print("\n Введенная матрица: ")
for i, lenght in enumerate(matrix):
    string = "".join([f"{e:^10}" for e in lenght])
    print(f"matrix[{i}] = {string}")

max_repeats = 0
max_row_index = -1

for i, row in enumerate(matrix):
    current_max = 1
    current_count = 1
    for j in range(1, len(row)):
        if row[j] == row[j - 1]:
            current_count += 1
        else:
            current_max = max(current_max, current_count)
            current_count = 1
    current_max = max(current_max, current_count)
    if current_max > max_repeats:
        max_repeats = current_max
        max_row_index = i


print(
    f"Строка с наибольшим количеством повторяющихся символов: {matrix[max_row_index]}"
)
