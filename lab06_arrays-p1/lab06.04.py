"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #6, Задание - 4, Вариант - 2
Задание: Найти наиболее длинную непрерывную возрастающая последовательность чётных чисел
"""

import math

# создаем массив чисел
stop = ""
my_list: list = []
print("Для того что-бы остановить сделайте пустой ввод.")
while True:
    num = input("Введите числа: ")
    if num == stop:
        print("Вы остановили ввод.")
        break
    else:
        my_list.append(int(num))
print(f"Ваш список: {my_list}")

current_length = 0
prev_even = float(-math.inf)

# расчет
for i in my_list:
    if i % 2 == 0:
        if i > prev_even:
            current_length += 1
        else:
            current_length = 1
        prev_even = i
    else:
        current_length = 0

print(f"Максимальная длина: {current_length}")
