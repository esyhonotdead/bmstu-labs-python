"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #6, Задание - 3
Задание: Найти значение K-го экстремума в списке.
"""

import random

# задаем размер массива
while True:
    max_el = int(input("Введите число элементов в массиве: "))
    if max_el <= 0:
        print("Размер массива должен быть больше 0")
        continue
    else:
        break

# заполняем массив
arr: list = [random.randint(-10, 10) for n in range(max_el)]
print(f"Ваш массив: {arr}")
k = 0
num = int(input("K: "))

# вычисоение экстремума
for i in range(1, len(arr) - 1):
    if (arr[i] > arr[i - 1] and arr[i] > arr[i + 1]) or (
        arr[i] < arr[i - 1] and arr[i] < arr[i + 1]
    ):
        k += 1  # счетчик
        if k == num:
            print(f"Экстремум: {arr[i]}")
            break
else:
    print("Экстремумов не найдено")
