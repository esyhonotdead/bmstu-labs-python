"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #4, Вариант - 24
Задание:
1) Составить программу вычисления суммы ряда с точностью до члена ряда ε.
2) Необходимо вывести таблицу промежуточных вычислений с заданным шагом и результат вычисления.
"""


def sum_series(x, epsilon, step, max_n):
    # Инициализация переменных
    n = 1
    sum_result = 1
    term = 1 / (n**x)

    # Заголовок таблицы
    header = f"| {'Номер итерации':^17} | {'Значение текущего члена':^28} | {'Промежуточная сумма':^25} |"
    print("-" * len(header))
    print(header)
    print("-" * len(header))

    # Пока текущий член больше или равен epsilon, продолжаем
    while abs(term) >= epsilon and n <= max_n:
        term = 1 / (n**x)
        sum_result += term
        # Вывод таблицы по шагу
        if n % step == 0:
            print(f"| {n:^17} | {term:^28.7g} | {sum_result:^25.7g} |")
        n += 1
    print("-" * len(header))

    # Проверка на достижение суммы
    if abs(term) > epsilon:
        print(f"Сумма не вычислена на {n-1} операций.")
    else:
        print(f"Сумма бесконечного ряда {sum_result:.5g}, вычислена за {n-1} итераций.")


# Ввод данных:
max_n = int(input("Введите максимальное число итераций: "))
x = int(input("Введите степень ряда: "))
step = int(input("Ведите шаг печати: "))
epsilon = float(input("Введите точность: "))

sum_series(x, epsilon, step, max_n)
