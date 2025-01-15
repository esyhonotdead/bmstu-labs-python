"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #15, Задание - 3
Отсортировать файл с помощью алгоритма сортировки вставками.
"""

import struct
import random

RECORD_SIZE = 4


def insertion_sort(file_path):
    """
    Перемещаем указатель в конец файла
    Узнаем количество чисел
    Сравниваем текущее число с предыдущим
    Если предыдущее число больше текущего, то перемещаем предыдущее число на одну позицию вперед
    Повторяем пока не найдем место для текущего числа
    Записываем текущее число на найденное место
    Повторяем для всех чисел
    """
    with open(file_path, "r+b") as f:
        f.seek(0, 2)
        file_size = f.tell()
        num_records = file_size // RECORD_SIZE

        for i in range(1, num_records):
            f.seek(i * RECORD_SIZE)
            current_record = f.read(RECORD_SIZE)
            current_value = struct.unpack("i", current_record)[0]

            j = i - 1
            while j >= 0:
                f.seek(j * RECORD_SIZE)
                previous_record = f.read(RECORD_SIZE)
                previous_value = struct.unpack("i", previous_record)[0]

                if previous_value > current_value:
                    f.seek((j + 1) * RECORD_SIZE)
                    f.write(previous_record)
                    j -= 1
                else:
                    break

            f.seek((j + 1) * RECORD_SIZE)
            f.write(current_record)


def main():
    file_path = "./out3.bin"
    numbers = [random.randint(-50, 50) for _ in range(15)]
    with open(file_path, "wb") as f:
        for num in numbers:
            f.write(struct.pack("i", num))
    print("До сортировки:", *numbers)

    insertion_sort(file_path)

    with open(file_path, "rb") as f:
        sorted_numbers = []
        num = f.read(RECORD_SIZE)
        while num:
            sorted_numbers.append(struct.unpack("i", num)[0])
            num = f.read(RECORD_SIZE)
    print("После сортировки:", *sorted_numbers)


if __name__ == "__main__":
    main()
