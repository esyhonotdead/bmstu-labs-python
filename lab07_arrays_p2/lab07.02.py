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
three_multiple = 0

# считаем числа кратные 3
for i in range(len(arr)):
    if abs(arr[i]) % 3 == 0:
        three_multiple += 1

# расширяем список
arr.extend([0] * three_multiple)

index = len(arr) - 1  # индекс для записи в расширенном списке
for i in range(len(arr) - three_multiple - 1, -1, -1):
    if arr[i] % 3 == 0:
        arr[index] = arr[i] * 2
        index -= 1
    arr[index] = arr[i]  # перемещение элемента
    index -= 1

print(f"Новый массив {arr}")
