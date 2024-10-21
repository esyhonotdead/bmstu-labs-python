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

max_sequence = []
current_length = []
prev_even = float(-math.inf)

# расчет
for num in arr:
    if num % 2 == 0:
        if not current_length or num > current_length[-1]:
            current_length.append(num)
        else:
            current_length = [num]
    else:
        current_length = []
    if len(current_length) > len(max_sequence):
        max_sequence = current_length[:]

print(f"Максимальная длина: {max_sequence}")
