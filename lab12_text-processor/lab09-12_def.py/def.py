"""
Дан текст в txt файле. Найти предлоэение в котором наибольшее число знаков препинани. Весь файл считвыать нельзя.
"""

import string


def sum_punctuation(sentence):
    punctuation_marks = set(string.punctuation)
    return sum(1 for char in sentence if char in punctuation_marks)


def most_punctuation(file_path):
    max_punctuation_count = 0
    sentence_with_most_punctuation = ""
    buffer = ""

    with open(file_path, "r", encoding="UTF-8") as file:
        while True:
            char = file.read(1)
            print(char)
            if not char:
                break
            buffer += char
            print(buffer)
            if char in ".!?":
                punctuation_count = sum_punctuation(buffer)
                if punctuation_count > max_punctuation_count:
                    max_punctuation_count = punctuation_count
                    sentence_with_most_punctuation = buffer
                buffer = ""

    return (
        sentence_with_most_punctuation.strip()
        + " кол-во: "
        + str(max_punctuation_count)
    )


def main():
    file_path = "./in.txt"
    result = most_punctuation(file_path)
    print("Предложение с наибольшим числом знаков препинания:")
    print(result)


if __name__ == "__main__":
    main()
