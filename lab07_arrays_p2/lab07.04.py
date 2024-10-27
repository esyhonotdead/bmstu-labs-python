"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #7, Задание - 4, Вариант - 6
Задание: Замена двух подряд идущих цифр на последнюю цифру их суммы.
"""

n = int(input("Введите длину списка: "))
while n <= 0:
    print("Ошибка: введите положительное целое число.")
    n = input("Введите длину списка: ")

arr = []
for i in range(n):
    element = input(f"Введите строку {i + 1}: ")
    arr.append(element)

digits = [str(x) for x in range(1, 10)]

"""
arr = ["123abc", "abc123", "a12b23c45d", "ab123cd123ed123"]  test cases
      ["33abc", "abc33", "a3b5c9d, "ab33cd33ed33"] answers
"""

if not arr:
    print("Введен пустой список")
else:
    print("\nВведенный список строк:")
    for i in arr:
        print(i, end=" ")

    for i in range(len(arr)):
        current_string = arr[i]
        new_string = ""
        index = 0

        while index < len(current_string):
            if (
                index < len(current_string) - 1
                and current_string[index] in digits
                and current_string[index + 1] in digits
            ):
                digit1 = int(current_string[index])
                digit2 = int(current_string[index + 1])
                sum_last_digit = (digit1 + digit2) % 10

                new_string += str(sum_last_digit)
                index += 2

            else:
                new_string += current_string[index]
                index += 1

        # заменяем строку на новую
        arr[i] = new_string
    print("\nИзмененный список строк:")
    for i in arr:
        print(i, end=" ")
