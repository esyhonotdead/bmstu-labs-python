"""Вводиться список целых чисел заменить второе по величине значение на среднее арифмтетическое положительных чисел(по массиву можно пройтим только 1 раз)"""

arr: list = [-10, 3, 5, 2, 7, -12, 15, 12, 12]
print(arr)

first_max_num = second_max_num = float("-inf")
positive_sum = sum_count = 0

for i in arr:
    if i > 0:
        positive_sum += i  # сумма всех полож. чисел
        sum_count += 1  # кол-во полож. чисел

    # если i больше первого наибольшего числа то i становиться первым, если нет то проверяется равенство между числом, первым и вторым наибольшими числами
    if i > first_max_num:
        second_max_num = first_max_num
        first_max_num = i
    elif second_max_num < i < first_max_num:
        second_max_num = i

average_positive = (
    positive_sum / sum_count if sum_count > 0 else 0
)  # среднее арифмитическое полож. чисел

arr = [
    average_positive if x == second_max_num else x for x in arr
]  # проверяет если значение в массиве соотвествует наибольшему второму числу и заменяет его на сред арифмитическое и вывод список

print(positive_sum)
print(sum_count)

print(average_positive)
print(second_max_num)

print(arr)
