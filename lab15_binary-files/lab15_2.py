"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #15, Задание - 2, Вариант - 3
После каждого нечётного числа, добавить его удвоенное значение.
"""

import struct

file_path = "./out2.bin"
numbers = map(int, input("Введите числа через пробел: ").split(" "))
with open(file_path, "wb") as f:
    for num in numbers:
        f.write(struct.pack("i", num))


with open(file_path, "rb") as file:
    """
    Функция запоминает в массив позиции для удаления
    """
    n = 0
    positions_to_delete = []
    num = file.read(4)  # int = 4byte
    while num:
        current = struct.unpack("i", num)[0]
        if current % 2 != 0:
            positions_to_delete.append(n)
        n += 1
        num = file.read(4)


def add_line(filename: str, n: int):
    """
    Добавляем строку для сдвига и копирования
    """
    with open(filename, "r+b") as file:
        file.seek(0, 2)
        file.seek(file.tell() - 4)
        lower_line = file.read(4)
        file.write(lower_line)
        file.seek(n * 4)
        current = file.read(4)
        next_line = file.read(4)
        while next_line:
            file.seek(file.tell() - 4)
            file.write(current)
            current = next_line
            next_line = file.read(4)

        file.seek(n * 4)
        num = struct.unpack("i", file.read(4))[0]
        file.write(struct.pack("i", num * 2))


def main():
    for i in positions_to_delete[::-1]:
        add_line(file_path, i)
    print("Обновлённый файл:", end=" ")
    with open(file_path, "rb") as file:
        num = file.read(4)
        while num:
            print((struct.unpack("i", num))[0], end=" ")
            num = file.read(4)


if __name__ == "__main__":
    main()
