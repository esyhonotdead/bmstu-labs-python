"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #4, Вариант - 24
Задание:
1) Написать программу для вывода значения функции в таблицу (вводные данные: начальное и конечное значение аругмента, шаг разбиения аргумента)
2) Построить график одной из функций
"""

import math

# ввод занчений
while True:
    x_init = int(input("x нач: "))
    x_end = int(input("x конеч: "))
    step = int(input("шаг: "))
    if x_init <= 0 and x_end < 0 and step < 0:
        continue
    else:
        break

# таблица
header = f"| {'Аргумент':^10} | {'Функция #1':^15} | {'Функция #2':^15} | {'Функция #3':^15} |"
print("-" * len(header))
print(header)
print("-" * len(header))

for x in range(x_init, x_end, step):
    y1 = math.pow(x, 2) - 4 * x
    y2 = math.pow(x, 3) - 3 * math.pow(x, 2) + 1
    y3 = (y1 + y2) / 10
    print(f"| {x:^10} | {y1:^15.5g} | {y2:^15.5g} | {y3:^15.5g} |")


print("-" * len(header))

# график
