"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #7, Задание - 3, Вариант - 1
Задание: Поиск элемента с наибольшим числом английских гласных букв.
"""

n = int(input("Введите длину списка: "))
while n <= 0:
    print("Ошибка: введите положительное целое число.")
    n = int(input("Введите длину списка: "))

arr = []
for i in range(n):
    element = input(f"Введите элемент {i + 1}: ")
    arr.append(element)

vowels = "aeyuioe"
vowels_count = 0
vowels_coun_previous = float("-inf")

for i in range(n):
    word = arr[i]
    for char in word:
        if char.lower() in vowels:  # подгоняем под стандарт
            vowels_count += 1
    if vowels_count > vowels_coun_previous:
        # конечный вывод
        vowels_count = vowels_coun_previous
        word_result = word

print(
    f"Эелемент с самым большим количеством гласных {word_result}, с {vowels_count} символов."
)
