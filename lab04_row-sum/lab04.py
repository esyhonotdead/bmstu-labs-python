"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #4, Вариант - 24
Задание:
1) Составить программу вычисления суммы ряда с точностью до члена ряда ε.
2) Необходимо вывести таблицу промежуточных вычислений с заданным шагом и результат вычисления.
"""

# Нормальные таблицы
from prettytable import PrettyTable


def sum_series(x, epsilon, step, max_n):
    # Инициализация переменных
    n = 1
    sum_result = 1
    term = 1 / (n**x)
    my_table = PrettyTable(["# Итерации", "t", "y"])
    my_table.add_row([n, term, sum_result])

    # Пока текущий член больше или равен epsilon, продолжаем
    while abs(term) >= epsilon and n <= max_n:
        term = 1 / (n**x)
        sum_result += term
        if n % step == 0:
            term_temp = float(f"{term:.5g}")
            sum_result_temp = float(f"{sum_result:.5g}")
            my_table.add_row([n, term_temp, sum_result_temp])
        n += 1
    print(my_table)
    if abs(term) > epsilon:
        print(f"Сумма не вычеслена на {n-1} операций.")
    else:
        print(f"Сумма бесконечного ряда {sum_result:.5g}, вычислена за {n-1} итераций.")


# Ввод данных:
max_n = int(input("Введите максимальное число итераций: "))
x = int(input("Введите степень ряда: "))
step = int(input("Ведите шаг печати: "))
epsilon = float(input("Введите точность: "))
sum_series(x, epsilon, step, max_n)
