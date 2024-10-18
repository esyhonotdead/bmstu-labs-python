"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #6, Задание - 5, Вариант - 7
Задание: Поменять местами последний нулевой и максимальный отрицательный элемент
"""

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

# индекс последнего нулевого
last_zero_index = -1
for i in range(len(arr)):
    if arr[i] == 0:
        last_zero_index = i

# индекс минимального числа
max_negative_index = -1
max_negative = float("-inf")
for i in range(len(arr)):
    if arr[i] < 0 and arr[i] > max_negative:
        max_negative = arr[i]
        max_negative_index = i

# меняем места элементы
if last_zero_index != -1 and max_negative_index != -1:
    arr[last_zero_index], arr[max_negative_index] = (
        arr[max_negative_index],
        arr[last_zero_index],
        print(f"Ваш новый список: {arr}"),
    )
else:
    print("Нечего менять")
