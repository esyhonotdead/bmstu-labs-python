"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #4, Вариант - 24
Составить программу вычисления суммы ряда (по варианту) с точностью до члена ряда ε.
Необходимо вывести таблицу промежуточных вычислений с заданным шагом и результат вычисления.
"""

# Нормальные таблицы
from prettytable import PrettyTable


def sum_series(x, epsilon, step):
    # Инициализация переменных
    n = 1
    sum_result = 1
    term = 1 / (n**x)
    my_table = PrettyTable(["# Итерации", "t", "y"])
    my_table.add_row([n, round(term, 3), round(sum_result, 3)])

    # Пока текущий член больше или равен epsilon, продолжаем
    while abs(term) >= epsilon:
        term = 1 / (n**x)
        sum_result += term
        if n % step == 0:
            my_table.add_row([n, round(term, 5), round(sum_result, 5)])
        n += 1
    print(my_table)
    print(f"Сумма бесконечного ряда {round(sum_result, 5)}, вычислена за {n} итераций.")


# Ввод данных:
x = int(input("Введите степень ряда: "))
step = int(input("введите шаг печати: "))
epsilon = float(input("Введите точность: "))
sum_series(x, epsilon, step)
