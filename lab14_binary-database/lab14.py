"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #14
Задание:
Требуется написать программу, которая позволит с помощью меню выполнить
следующие действия:
1. Выбрать файл для работы
2. Инициализировать базу данных (создать либо перезаписать файл и заполнить
его записями)
3. Вывести содержимое базы данных
4. Добавить запись в произвольное место базы данных (пользователь указывает
номер позиции, в которую должна быть вставлена запись)
5. Удалить произвольную запись из базы данных (пользователь указывает номер
удаляемой записи)
6. Поиск по одному полю
7. Поиск по двум полям
Тематика базы данных - фиксированная, выбираемая на усмотрение исполнителя.
Давать пользователю создавать БД произвольной структуры не требуется.
Записи должны состоять из 3-4 полей разных типов (текстовые, числовые). Для
формирования записей фиксированного размера (структур) в бинарном формате
следует использовать модуль struct.
Поля для поиска в пп. 6 и 7 выбираются на усмотрение исполнителя.
"""

import os
import struct

test_data = [
    "Anton;23;1;1.82",
    "Ivan;23;1;1.85",
    "Masha;25;0;1.64",
    "Daria;17;0;1.58",
    "Vlad;23;1;1.75",
    "Anna;21;0;1.80",
    "Sergey;30;1;1.90",
]


def choose_db():
    counter = 0
    db_path = os.path.join(os.getcwd(), "databases")
    for db in os.listdir(db_path):
        if db.endswith(".bin"):
            counter += 1
            print(f"{counter}. {db}")
    if counter == 0:
        print("Базы данных не найдены.")
        return None
    var = int(input("Выберите файл: "))
    flag = True
    while flag:
        if 1 <= var <= counter:
            flag = False
            return os.listdir(db_path)[var - 1]
        else:
            print("Неверный ввод, попробуйте снова.")


def init_db(db):
    if db is None:
        name = input("Введите имя для базы данных: ")
        with open(f"databases/{name}.bin", "wb") as f:
            for record in test_data:
                line = record.split(";")
                name = line[0].encode("utf-8")
                age = int(line[1])
                studient = bool(int(line[2]))
                height = float(line[3])
                f.write(struct.pack("10si?d", name, age, studient, height))
    else:
        with open(f"databases/{db}", "wb") as f:
            for record in test_data:
                line = record.split(";")
                name = line[0].encode("utf-8")
                age = int(line[1])
                studient = bool(int(line[2]))
                height = float(line[3])
                f.write(struct.pack("10si?d", name, age, studient, height))


def read_db(db):
    if db is None:
        print("База данных не выбрана.")
        return
    with open(f"databases/{db}", "rb") as f:
        while True:
            data = f.read(32)
            if not data:
                break
            name, age, studient, height = struct.unpack("10si?d", data)
            print(f"{name.decode('utf-8')};{age};{studient};{height}")


def add_record(db):
    if db is None:
        print("База данных не выбрана.")
        return

    with open(f"databases/{db}", "rb") as f:
        data = f.read()
    with open(f"databases/{db}", "wb") as f:
        pos = int(input("Введите номер позиции: "))
        for i in range(0, len(data), 32):
            if i == pos * 32:
                line = input("Введите запись: ")
                line = line.split(";")
                name = line[0].encode("utf-8")
                age = int(line[1])
                studient = bool(int(line[2]))
                height = float(line[3])
                f.write(struct.pack("10si?d", name, age, studient, height))
            f.write(data[i : i + 32])


def delete_record(db):
    if db is None:
        print("База данных не выбрана.")
        return
    with open(f"databases/{db}", "rb") as f:
        data = f.read()
    with open(f"databases/{db}", "wb") as f:
        pos = int(input("Введите номер позиции: "))
        for i in range(0, len(data), 32):
            if i != pos * 32:
                f.write(data[i : i + 32])


def search_one_field(db):
    if db is None:
        print("База данных не выбрана.")
        return
    with open(f"databases/{db}", "rb") as f:
        value = input("Введите значение для поиска: ")
        while True:
            data = f.read(32)
            if not data:
                break
            name, age, studient, height = struct.unpack("10si?d", data)
            if value in name.decode("utf-8"):
                print(f"{name.decode('utf-8')};{age};{studient};{height}")
            elif value == str(age):
                print(f"{name.decode('utf-8')};{age};{studient};{height}")
            elif value == str(studient):
                print(f"{name.decode('utf-8')};{age};{studient};{height}")
            elif value == str(height):
                print(f"{name.decode('utf-8')};{age};{studient};{height}")


def seraсh_two_fields(db):
    if db is None:
        print("База данных не выбрана.")
        return
    with open(f"databases/{db}", "rb") as f:
        value1 = input("Введите значение для поиска: ")
        value2 = input("Введите второе значение для поиска: ")
        while True:
            data = f.read(32)
            if not data:
                break
            name, age, studient, height = struct.unpack("10si?d", data)
            if value1 in [name.decode("utf-8"), str(age), str(studient), str(height)]:
                if value2 in [
                    name.decode("utf-8"),
                    str(age),
                    str(studient),
                    str(height),
                ]:
                    print(f"{name.decode('utf-8')};{age};{studient};{height}")


def menu():
    db = choose_db()
    while True:
        print(f"Текущая база данных {db}")
        print("1. Выбрать файл для работы")
        print("2. Инициализировать базу данных")
        print("3. Вывести содержимое базы данных")
        print("4. Добавить запись по номеру позиции")
        print("5. Удалить запись по номеру позиции")
        print("6. Поиск по одному полю")
        print("7. Поиск по двум полям")
        print("8. Выход")
        var = input("Выберите опцию: ")
        match var:
            case "1":
                db = choose_db()
            case "2":
                init_db(db)
            case "3":
                read_db(db)
            case "4":
                add_record(db)
            case "5":
                delete_record(db)
            case "6":
                search_one_field(db)
            case "7":
                seraсh_two_fields(db)
            case "8":
                break
            case _:
                print("Неверный ввод, попробуйте снова.")


menu()
