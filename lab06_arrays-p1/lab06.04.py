"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #6, Задание - 4, Вариант - 2
Задание: Найти наиболее длинную непрерывную возрастающая последовательность чётных чисел
"""

import math

# создаем массив чисел
stop = ""
arr: list = []
print("Для того что-бы остановить сделайте пустой ввод.")
while True:
    num = input("Введите числа: ")
    if num == stop:
        print("Вы остановили ввод.")
        break
    else:
        arr.append(int(num))
print(f"Ваш список: {arr}")

current_length = 0
prev_even = float(-math.inf)
sequence: list = []

# расчет
for i in arr:
    if i % 2 == 0:
        if i > prev_even:
            current_length += 1
            sequence.append(i)
        else:
            current_length = 1
        prev_even = i
    else:
        current_length = 0

print(f"Максимальная длина: {current_length}")
print("Ваша последовательность: ", end="")
for i in sequence:
    print(i, end=",")
