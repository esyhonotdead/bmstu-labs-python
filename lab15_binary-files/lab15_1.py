"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #15, Задание - 1, Вариант - 5
Удалить все отрицательные числа, за один проход по файлу
"""

import struct
import random

RECORD_SIZE = 4


def remove_negatives(file_path: str):
    """
    Побитово читаем строку и записываем по условию
    """
    read_pointer = 0
    pos = 0

    with open(file_path, "r+b") as f:
        num = f.read(RECORD_SIZE)
        while num:
            number = struct.unpack("i", num)[0]
            if number >= 0:
                f.seek(pos)
                f.write(struct.pack("i", number))
                pos += RECORD_SIZE

            read_pointer += RECORD_SIZE
            f.seek(read_pointer)
            num = f.read(RECORD_SIZE)
        f.truncate(pos)


def main():
    file_path = "./out1.bin"
    numbers = [random.randint(-50, 50) for _ in range(15)]
    with open(file_path, "wb") as f:
        for num in numbers:
            f.write(struct.pack("i", num))
    print("До удаления отрицательных чисел:", *numbers)
    remove_negatives(file_path)

    with open(file_path, "rb") as f:
        updated_numbers = []
        num = f.read(4)
        while num:
            updated_numbers.append(struct.unpack("i", num)[0])
            num = f.read(4)
    print("После удаления:", *updated_numbers)


if __name__ == "__main__":
    main()
