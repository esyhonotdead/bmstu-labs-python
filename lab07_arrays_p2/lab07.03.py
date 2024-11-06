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

vowels = "aeyuoi"
vowels_count_previous = float("-inf")
result_word: str

for i in range(n):
    vowels_count = 0
    word = arr[i]
    for char in word:
        if char.lower() in vowels:  # подгоняем под стандарт
            vowels_count += 1
    if vowels_count >= vowels_count_previous:
        vowels_count_previous = vowels_count
        result_word = arr[i]
    else:
        continue

print(
    f"Элемент с наибольшем числом гласных букв: {result_word}, с числом: {vowels_count_previous}"
)
