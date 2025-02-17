"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #4, Вариант - 24
Задание:
1) Написать программу для вывода значения функции в таблицу (вводные данные: начальное и конечное значение аругмента, шаг разбиения аргумента)
2) Построить график функции y3
3) Найти y3 min и xmin при котором оно достигается
"""

import math

# ввод значений
while True:
    x_start = float(input("Введите начальное значение x: "))
    x_end = float(input("Введите конечное значение x: "))
    step = float(input("Введите шаг: "))
    if x_start <= 0 and x_end < 0 or step < 0:
        print("Пожалуйста, введите корректные значения.")
        continue
    else:
        break

# таблица
header = f"| {'Аргумент':^10} | {'Функция #1':^15} | {'Функция #2':^15} | {'Функция #3':^15} |"
print("-" * len(header))
print(header)
print("-" * len(header))

x_count = int((x_end - x_start) / step)

# данные таблицы

x_count = int((x_end - x_start) / step)
for i in range(x_count + 1):
    x = i * step + x_start
    y1 = math.pow(x, 2) - 4 * x  # Функция #1
    y2 = math.pow(x, 3) - 3 * math.pow(x, 2) + 1  # Функция #2
    y3 = (y1 + y2) / 10  # Функция #3
    print(f"| {x:^10g} | {y1:^15.3g} | {y2:^15.3g} | {y3:^15.3g} |")

print("-" * len(header))

# минимальное значения функции y3
y3_min = y3 = (
    math.pow(x_start, 2)
    - 4 * x_start
    + math.pow(x_start, 3)
    - 3 * math.pow(x_start, 2)
    + 1
) / 10

# максимальное значение y3
y3_max = (
    math.pow(x_end, 2) - 4 * x_end + math.pow(x_end, 3) - 3 * math.pow(x_end, 2) + 1
) / 10

# доп. задание
print("")
print(f"Минимальное значение y3 = {y3_min}, при x = {x_start}.")
print(f"Максимальное значение y3 = {y3_max}, при x = {x_end}.")
print("")

# засечеки
while True:
    num_ticks = int(input("Введите количество засечек на оси ординат (от 4 до 8): "))
    print("")
    if 4 <= num_ticks <= 8:
        break
    else:
        print("Пожалуйста, введите значение от 4 до 8.")

# график
width = 150  # ширина графика
scale_y = (y3_max - y3_min) / (width - 1)  # масштабирование по оси Y

# линейка для оси ординат
tick_step = (y3_max - y3_min) / (num_ticks - 1)
print(" " * 13, end="|")
space = width / num_ticks
print(int(space), end="")

for i in range(num_ticks):
    tick_value = y3_min + i * tick_step
    print(
        f"{tick_value:.3g}" + "_" * (int(space) - (len(f"{tick_value:.3g}")) + 4),
        end="",
    )

print("|")

# построение графика
for i in range(x_count + 1):
    x = i * step + x_start
    # x слева
    print(f"{x:<13.3g}|", end="")

    # значения y3
    y1 = math.pow(x, 2) - 4 * x
    y2 = math.pow(x, 3) - 3 * math.pow(x, 2) + 1
    y3 = (y1 + y2) / 10
    pos = int((y3 - y3_min) / scale_y)

    # пересекает ли ось абсцисс
    if y3_min <= 0 <= y3_max:
        zero_pos = int(-y3_min / scale_y)
        if pos == zero_pos:
            print(" " * pos + "*")
        elif pos < zero_pos:
            print(" " * pos + "*" + " " * (zero_pos - pos - 1) + "|")
        else:
            print(" " * zero_pos + "|" + " " * (pos - zero_pos - 1) + "*")
    else:
        print(" " * pos + "*")
