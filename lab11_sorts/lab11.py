"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #11
Задание:
Написать программу для демонстрации работы метода сортировки на примере массива целых чисел.
"""

import time
import random
from prettytable import PrettyTable


def insertion_sort(arr) -> tuple[list, int]:
    swap_count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            swap_count += 1
        if j != i - 1:
            swap_count += 1
        arr[j + 1] = key
    return (
        arr,
        swap_count,
    )


def sort_stat(arr_to_sort, sort_method=insertion_sort) -> tuple[list, float, int]:
    start_time = time.time()
    arr, swap_count = sort_method(arr_to_sort)
    end_time = time.time()

    elapsed_time = end_time - start_time
    if len(str(elapsed_time)) > 8:
        elapsed_time = f"{int(elapsed_time * 10**6)} mcs"

    return arr, elapsed_time, swap_count


def arr_lenght() -> int:
    while True:
        try:
            n = int(input("Введите длину массива:"))
            return n
        except ValueError:
            print("Введены неправильные данные.")


def sort_table(
    stat_n1,
    stat_n2,
    stat_n3,
    rev_stat_n1,
    rev_stat_n2,
    rev_stat_n3,
    rand_stat_n1,
    rand_stat_n2,
    rand_stat_n3,
):
    table = PrettyTable()
    table.field_names = [
        "Таблица",
        "Время N1",
        "Перестановки N1",
        "Время N2",
        "Перестановки N2",
        "Время N3",
        "Перестановки N3",
    ]
    table.add_row(
        [
            "Упорядоченный массив",
            f"{stat_n1[1]}",
            f"{stat_n1[2]}",
            f"{stat_n2[1]}",
            f"{stat_n2[2]}",
            f"{stat_n3[1]}",
            f"{stat_n3[2]}",
        ]
    )
    table.add_row(
        [
            "Обратный упорядоченный массив",
            f"{rev_stat_n1[1]}",
            f"{rev_stat_n1[2]}",
            f"{rev_stat_n2[1]}",
            f"{rev_stat_n2[2]}",
            f"{rev_stat_n3[1]}",
            f"{rev_stat_n3[2]}",
        ]
    )
    table.add_row(
        [
            "Случайный массив",
            f"{rand_stat_n1[1]}",
            f"{rand_stat_n1[2]}",
            f"{rand_stat_n2[1]}",
            f"{rand_stat_n2[2]}",
            f"{rand_stat_n3[1]}",
            f"{rand_stat_n3[2]}",
        ]
    )
    return table


def table_data(n: str):
    print(f"Массивы {n}")
    ln = arr_lenght()
    arr = [i for i in range(ln)]
    rev_arr = arr[::-1]
    rand_arr = [random.randint(-100, 100) for i in range(ln)]
    return arr, rev_arr, rand_arr


def foramt_time(sort_stat): ...


def main():
    rand_arr = [random.randint(-10, 10) for i in range(15)]
    print(f"Изначальный массив: {rand_arr}")
    rand_sort_stat = sort_stat(rand_arr, insertion_sort)
    print(
        f"Время сортировки {rand_sort_stat[1]}, количество перестановок: {rand_sort_stat[2]}"
    )
    print(f"Отсортированный массив: {rand_sort_stat[0]} \n")

    data_n1 = table_data("N1")
    data_n2 = table_data("N2")
    data_n3 = table_data("N3")

    sort_stat_arr_n1 = sort_stat(data_n1[0])
    sort_stat_arr_n2 = sort_stat(data_n2[0])
    sort_stat_arr_n3 = sort_stat(data_n3[0])
    sort_stat_rev_arr_n1 = sort_stat(data_n1[1])
    sort_stat_rev_arr_n2 = sort_stat(data_n2[1])
    sort_stat_rev_arr_n3 = sort_stat(data_n3[1])
    sort_stat_rand_arr_n1 = sort_stat(data_n1[2])
    sort_stat_rand_arr_n2 = sort_stat(data_n2[2])
    sort_stat_rand_arr_n3 = sort_stat(data_n3[2])

    print(
        sort_table(
            sort_stat_arr_n1,
            sort_stat_arr_n2,
            sort_stat_arr_n3,
            sort_stat_rev_arr_n1,
            sort_stat_rev_arr_n2,
            sort_stat_rev_arr_n3,
            sort_stat_rand_arr_n1,
            sort_stat_rand_arr_n2,
            sort_stat_rand_arr_n3,
        )
    )


if __name__ == "__main__":
    main()
