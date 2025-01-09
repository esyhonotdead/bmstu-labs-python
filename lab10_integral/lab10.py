"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #10
Задание:
Требуется написать программу для вычисления приближённого значения интеграла
известной, заданной в программе, методами правых прямоугольников и парабол.
Построить таблицу значений при вычислениях. По заданной первообразной определить,
какой метод является наиболее точным. Вывести таблицу абсолютных и относительных значений погрешности.
У наименее точного метода определить количество разбиений для достижения заданной точности.
"""

import math
from prettytable import PrettyTable


def input_value(name, is_int=True):
    while True:
        try:
            value = (
                float(input(f"Введите {name}: "))
                if not is_int
                else int(input(f"Введите {name}: "))
            )
            return value
        except ValueError:
            print("Неправильно введены данные.")


def num_table_format(value):
    try:
        value = f"{value:.5g}"
    except ValueError:
        value = "-"
    return value


def per_table_format(value):
    try:
        value = f"{value:.2%}"
    except ValueError:
        value = "-"
    return value


def integral_function(x):
    return 2 * math.pow(x, 2) + 1 / math.sqrt(math.log(x, 2))


def primitive_function(x):
    return math.pow(x, 3) / 3


def right_rectangle_method(func, start, end, npoints):
    dx = (end - start) / npoints
    result = 0
    for i in range(npoints):
        result += dx * func(start + dx)
        start += dx
    return result


def simpsons_method(func, start, end, npoints):
    if npoints % 2 != 0:
        return "-"
    else:
        dx = (end - start) / npoints
        result = 0
        for i in range(npoints):
            result += (
                dx
                / 6
                * (func(start) + 4 * func((2 * start + dx) / 2) + func(start + dx))
            )
            start += dx
    return result


def create_integration_table(n1, n2, rrm1, rrm2, sm1, sm2):
    table = PrettyTable()
    table.field_names = ["Метод/Кол-во разбиений", n1, n2]
    table.add_row(["Метод правых прямоугольников", f"{rrm1}", f"{rrm2}"])
    table.add_row(["Метод парабол", f"{sm1}", f"{sm2}"])
    return table


def create_error_table(
    rrm1_a, rrm2_a, sm1_a, sm2_a, rrm1_r, rrm2_r, sm1_r, sm2_r, n1, n2
):
    table = PrettyTable()
    table.field_names = ["Метод/Погрешность", "Абсолютная", "Относительная"]
    table.add_row(
        [
            f"Метод правых прямоугольников {n1}/{n2}",
            f"{rrm1_a}/{rrm2_a}",
            f"{rrm1_r}/{rrm2_r}",
        ]
    )
    table.add_row(
        [
            f"Метод парабол {n1}/{n2}",
            f"{sm1_a}/{sm2_a}",
            f"{sm1_r}/{sm2_r}",
        ]
    )
    return table


def real_value(primitive, start, end):
    return primitive(end) - primitive(start)


def absolute_error(real, approx):
    return abs(real - approx)


def relative_error(abs_error, real):
    return abs_error / real


def find_n(func, acc):
    n = 2
    integral = func(n)
    while True:
        new_integral = func(n * 2)
        if abs(integral - new_integral) <= acc:
            return n, new_integral
        integral = new_integral
        n *= 2


def main():
    start = input_value("начало отрезка", is_int=False)
    end = input_value("конец отрезка", is_int=False)
    flag = False
    while not flag:
        if start > end:
            end = input_value("конец отрезка", is_int=False)
        else:
            flag = True

    n1 = input_value("N1 участков разбиения", is_int=True)
    n2 = input_value("N2 участков разбиения", is_int=True)
    print()

    rrm1 = right_rectangle_method(integral_function, start, end, n1)

    rrm2 = right_rectangle_method(integral_function, start, end, n2)
    sm1 = simpsons_method(integral_function, start, end, n1)
    sm2 = simpsons_method(integral_function, start, end, n2)

    rrm1_table = num_table_format(rrm1)
    rrm2_table = num_table_format(rrm2)
    sm1_table = num_table_format(sm1)
    sm2_table = num_table_format(sm2)

    print(
        create_integration_table(
            "N1", "N2", rrm1_table, rrm2_table, sm1_table, sm2_table
        )
    )
    print()

    real = real_value(primitive_function, start, end)

    rrm1_abs_err = absolute_error(real, rrm1)
    rrm1_abs_err_table = num_table_format(rrm1_abs_err)
    rrm2_abs_err = absolute_error(real, rrm2)
    rrm2_abs_err_table = num_table_format(rrm2_abs_err)

    try:
        sm1_abs_err = absolute_error(real, sm1)
    except TypeError:
        sm1_abs_err = "-"

    sm1_abs_err_table = num_table_format(sm1_abs_err)

    try:
        sm2_abs_err = absolute_error(real, sm2)
    except TypeError:
        sm2_abs_err = "-"

    sm2_abs_err_table = num_table_format(sm2_abs_err)

    rrm1_rel_err = relative_error(rrm1_abs_err, real)
    rrm1_rel_err_table = per_table_format(rrm1_rel_err)
    rrm2_rel_err = relative_error(rrm2_abs_err, real)
    rrm2_rel_err_table = per_table_format(rrm2_rel_err)
    try:
        sm1_rel_err = relative_error(sm1_abs_err, real)
    except TypeError:
        sm1_rel_err = "-"
    sm1_rel_err_table = per_table_format(sm1_rel_err)
    try:
        sm2_rel_err = relative_error(sm2_abs_err, real)
    except TypeError:
        sm2_rel_err = "-"
    sm2_rel_err_table = per_table_format(sm2_rel_err)

    try:
        if abs(rrm1_abs_err) > abs(sm1_abs_err):
            print(
                f"Метод парабол более точный, чем метод правых прямоугольников на разбиении {n1}."
            )
            less_acc_method = lambda n: right_rectangle_method(  # noqa: E731
                integral_function, start, end, n
            )
        else:
            print(
                f"Метод правых прямоугольников более точный, чем метод парабол на разбиении {n1}."
            )
            less_acc_method = lambda n: simpsons_method(  # noqa: E731
                integral_function, start, end, n
            )
    except TypeError:
        print(f"Невозможно сравнить функции на разибении {n1}")

    try:
        if abs(rrm2_abs_err) > abs(sm2_abs_err):
            print(
                f"Метод парабол более точный, чем метод правых прямоугольников на разбиении {n2}."
            )
            less_acc_method = lambda n: right_rectangle_method(  # noqa: E731
                integral_function, start, end, n
            )
        else:
            print(
                f"Метод правых прямоугольников более точный, чем метод парабол на разбиении {n2}."
            )
            less_acc_method = lambda n: simpsons_method(  # noqa: E731
                integral_function, start, end, n
            )
    except TypeError:
        print(f"Невозможно сравнить функции на разибении {n2}")

    print()
    print(
        create_error_table(
            rrm1_abs_err_table,
            rrm2_abs_err_table,
            sm1_abs_err_table,
            sm2_abs_err_table,
            rrm1_rel_err_table,
            rrm2_rel_err_table,
            sm1_rel_err_table,
            sm2_rel_err_table,
            n1,
            n2,
        )
    )
    print()

    try:
        acc = input_value("необходимую точность", is_int=False)
        curr_n, integral_value = find_n(less_acc_method, acc)
        print(
            f"Интеграл с заданной точностью вычисляется за {curr_n} разбиений и имеет значение {integral_value:.7g}"
        )
    except Exception:
        print("BRUH")


if __name__ == "__main__":
    main()
