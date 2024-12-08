"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #12
Задание:
Текстовый процессор
1) Сложение и вычитание.
2) Предложение, содержащее слово с максимальным количеством согласных букв.
"""

text = [
    "Я памятник себе воздвиг нерукотворный,",
    "К нему не зарастет народная тропа,",
    "Вознесся выше он главою непокорной",
    "Александрийского столпа.",
    "Нет, весь я не умру — душа в заветной лире 1000 - 7",
    "Мой прах переживет и тленья убежит —",
    "И славен буду я 17 + 34, доколь в подлунном мире",
    "Жив будет хоть один пиит.",
]


def is_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def math_expressions(expr):
    operators = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
    }
    current_num = ""
    operator = None
    stack = []

    for char in expr:
        if char.isdigit() or (char == "-" and not current_num):
            current_num += char
        elif char in operators:
            if current_num:
                stack.append(int(current_num))
                current_num = ""
            if len(stack) > 1 and operator:
                b = stack.pop()
                a = stack.pop()
                stack.append(operators[operator](a, b))
            operator = char
        elif char.strip() == "":
            continue
        else:
            return expr

    if current_num:
        stack.append(int(current_num))
        if len(stack) > 1 and operator:
            b = stack.pop()
            a = stack.pop()
            return str(operators[operator](a, b))
        return str(stack[0])

    return expr


def find_and_calculate_expressions(text):
    for i in range(len(text)):
        new_line = ""
        j = 0
        while j < len(text[i]):
            if text[i][j].isdigit() or (
                text[i][j] in "+-" and (j == 0 or text[i][j - 1] == " ")
            ):
                expr = ""
                while j < len(text[i]) and (
                    text[i][j].isdigit() or text[i][j] in "+- "
                ):
                    expr += text[i][j]
                    j += 1
                expr_result = math_expressions(expr)
                new_line += expr_result + " "
            else:
                new_line += text[i][j]
                j += 1
        text[i] = " ".join(new_line.split())


def align_left(text):
    max_len = max(len(line) for line in text)
    for i in range(len(text)):
        text[i] = text[i] + " " * (max_len - len(text[i]))


def align_right(text):
    max_len = max(len(line) for line in text)
    for i in range(len(text)):
        text[i] = " " * (max_len - len(text[i])) + text[i]


def align_center(text):
    max_len = max(len(line) for line in text)
    for i in range(len(text)):
        diff = max_len - len(text[i])
        average = text[i].count(" ")
        if average == 0:
            continue
        extra = diff // average
        residue = diff - extra * average
        string = ""
        for ch in text[i]:
            if ch == " ":
                string += " " * (1 + extra + (1 if residue > 0 else 0))
                residue = max(0, residue - 1)
            else:
                string += ch
        text[i] = string


def remove_word(text, word):
    for i in range(len(text)):
        text[i] = " ".join([w for w in text[i].split() if w != word])


def replace_word(text, old_word, new_word):
    for i in range(len(text)):
        text[i] = text[i].replace(old_word, new_word)


def remove_align(text):
    for i in range(len(text)):
        text[i] = " ".join(text[i].split())
    return text


def count_consonants(word):
    consonants = "бвгджзйклмнпрстфхцчшщ"
    return sum(1 for char in word.lower() if char in consonants)


def split_into_words(sentence):
    words = []
    word = ""
    for char in sentence:
        if char.isalnum():
            word += char
        elif word:
            words.append(word)
            word = ""
    if word:
        words.append(word)
    return words


def find_and_remove_sentence_with_max_consonants(text):
    max_consonants = 0
    max_index = -1
    result_sentence = ""

    for i, sentence in enumerate(text):
        words = split_into_words(sentence)
        for word in words:
            consonants_count = count_consonants(word)
            if consonants_count > max_consonants:
                max_consonants = consonants_count
                result_sentence = sentence
                max_index = i

    if max_index != -1:
        print(
            f"Предложение с максимальным количеством согласных букв: {result_sentence}"
        )
        text.pop(max_index)
    else:
        print("Предложение с максимальным количеством согласных не найдено.")


# Обновление меню
def print_menu():
    print("> 1. Выровнять текст по левому краю")
    print("> 2. Выровнять текст по правому краю")
    print("> 3. Выровнять текст по ширине")
    print("> 4. Удалить все вхождения заданного слова")
    print("> 5. Заменить одно слово другим")
    print("> 6. Вычислить арифметические выражения")
    print(
        "> 7. Найти предложение, содержащее слово с максимальным количеством согласных букв, и удалить его"
    )
    print("> 0. Завершить программу")


while True:
    print_menu()
    choice = input("Выберите пункт: ")

    if choice == "1":
        align_left(text)
        print("\nРезультат:")
        for line in text:
            print(line)
        text = remove_align(text)

    elif choice == "2":
        align_right(text)
        print("\nРезультат:")
        for line in text:
            print(line)
        text = remove_align(text)

    elif choice == "3":
        align_center(text)
        print("\nРезультат:")
        for line in text:
            print(line)
        text = remove_align(text)

    elif choice == "4":
        word_to_remove = input("Введите слово для удаления: ")
        remove_word(text, word_to_remove)
        print("\nРезультат:")
        for line in text:
            print(line)

    elif choice == "5":
        old_word = input("Введите слово для замены: ")
        new_word = input("Введите новое слово: ")
        replace_word(text, old_word, new_word)
        print("\nРезультат:")
        for line in text:
            print(line)

    elif choice == "6":
        find_and_calculate_expressions(text)
        print("\nРезультат:")
        for line in text:
            print(line)

    elif choice == "7":
        find_and_remove_sentence_with_max_consonants(text)
        print("\nОбновленный текст:")
        for line in text:
            print(line)

    elif choice == "0":
        print("Программа завершена.")
        break

    else:
        print("Неверный пункт. Повторите выбор.")
