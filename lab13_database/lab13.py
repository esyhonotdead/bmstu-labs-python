import os

test_data = """Anton;23;True;1.82\nIvan;12;True;1.85\nMasha;25;False;1.64\nDaria;17;False;1.58\n"""


def choose_db():
    counter = 0
    db_path = os.path.join(os.getcwd(), "databases")
    if not os.path.exists(db_path):
        os.makedirs(db_path)
    for db in os.listdir(db_path):
        if db.endswith(".txt"):
            counter += 1
            print(f"{counter}. {db}")
    if counter == 0:
        print("Базы данных не найдены.")
        return None
    var = int(input("Выберите файл: "))
    return os.listdir(db_path)[var - 1]


def init_db(db):
    db_path = os.path.join(os.getcwd(), "databases")
    if db is None:
        name = input("Введите имя для базы данных: ")
        with open(os.path.join(db_path, f"{name}.txt"), "w") as f:
            f.write(test_data)
    else:
        with open(os.path.join(db_path, db), "w") as f:
            f.write(test_data)


def read_db(db):
    db_path = os.path.join(os.getcwd(), "databases", db)
    with open(db_path, "r") as f:
        print(f.read())


def add_record(db):
    db_path = os.path.join(os.getcwd(), "databases", db)
    record = input("Введите новую запись (формат: Имя;Возраст;Статус;Рост): ")
    with open(db_path, "a") as f:
        f.write(record + "\n")


def search_one_field(db):
    field_to_find = input("Введите поле для поиска: ")
    db_path = os.path.join(os.getcwd(), "databases", db)
    with open(db_path, "r") as f:
        for line_number, line in enumerate(f, start=1):
            if field_to_find in line:
                print(f"Строка {line_number}: {line.strip()}")


def search_two_fields(db):
    fields_to_find = input(
        "Введите два поля для поиска, разделенные точкой с запятой: "
    ).split(";")
    if len(fields_to_find) != 2:
        print("Ошибка: необходимо ввести ровно два поля для поиска.")
        return

    db_path = os.path.join(os.getcwd(), "databases", db)
    with open(db_path, "r") as f:
        for line_number, line in enumerate(f, start=1):
            if fields_to_find[0] in line and fields_to_find[1] in line:
                print(f"Строка {line_number}: {line.strip()}")


def menu():
    db = choose_db()
    while True:
        print(f"Текущая база данных {db}")
        print("1. Выбрать файл для работы")
        print("2. Инициализировать базу данных")
        print("3. Вывести содержимое базы данных")
        print("4. Добавить запись")
        print("5. Поиск по одному полю")
        print("6. Поиск по двум полям")
        print("7. Выход")
        var = input("Choose an option: ")
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
                search_one_field(db)
            case "6":
                search_two_fields(db)
            case "7":
                break
            case _:
                print("error")


menu()
