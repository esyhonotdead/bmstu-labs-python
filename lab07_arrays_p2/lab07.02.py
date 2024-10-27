"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #7, Задание - 2, Вариант - 1
Задание: После каждого элемента целочисленного списка кратного 3, добавить его удвоенное значение.
"""

n = int(input("Введите длину списка: "))
while n <= 0:
    print("Ошибка: введите положительное целое число.")
    n = int(input("Введите длину списка: "))

arr = []
for i in range(n):
    element = int(input(f"Введите элемент {i + 1}: "))
    arr.append(element)

multiples_of_three = 0
for i in range(len(arr)):
    if arr[i] % 3:
        multiples_of_three += 1

arr += [0] * multiples_of_three  # расширяем массив


index = len(arr) - 1  # индекс для записи в расширенном списке
for i in range(len(arr) - multiples_of_three - 1, -1, -1):
    if arr[i] < 0:
        arr[index] = arr[i] * 2
        index -= 1
    arr[index] = arr[i]  # перемещение элемента
    index -= 1

# Вывод
print("Изменённый список: ", end="")
print(*arr)
