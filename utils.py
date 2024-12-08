"""
Тут я храню всякие утиль функции, они жестко + мощно закрывают все потребности в проверке кода
"""


def input_number(input_text: str, type: int | float) -> float | int | None:
    """
    Ввод числа с выбором типа.
    """
    while True:
        number = input(f"{input_text}: ")
        if type is int:
            try:
                number = int(number)
                return number
            except ValueError:
                print("Введите корректные данные.")
        elif type is float:
            try:
                number = int(number)
                return number
            except ValueError:
                print("Введите корректные данные.")
        else:
            return None
