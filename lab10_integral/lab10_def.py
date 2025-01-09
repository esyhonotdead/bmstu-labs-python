"""
3/8, серединные прямоугольнки, с заданным количеством итераций
"""


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


def integral_function(x):
    return 1 / x


def middle_rectangle_method(func, start, end, npoints):
    dx = (end - start) / npoints
    result = 0
    for i in range(npoints):
        result += func((i * dx + (i + 1) * dx) / 2 + start) * dx
    return result


def three_eights_method(func, start, end, npoints):
    if (npoints % 3 != 0) or (npoints < 3):
        return "Невозможно вычислить функцию на данном кол-ве разделений"
    dx = (end - start) / npoints
    result = func(start) + func(end)
    for i in range(1, npoints):
        if i % 3 == 0:
            result += 2 * func(start + dx * i)
        else:
            result += 3 * func(start + dx * i)
    return result * 3 / 8 * dx


def find_n(func, acc):
    n = 3
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

    npoints = input_value("N1 участков разбиения", is_int=True)
    middle_rectangle_result = middle_rectangle_method(
        integral_function, start, end, npoints
    )
    print(middle_rectangle_result)
    three_eights_result = three_eights_method(integral_function, start, end, npoints)
    print(three_eights_result)

    three_eights_method_findn = lambda n: three_eights_method(  # noqa: E731
        integral_function, start, end, n
    )
    middle_rectangle_method_findn = lambda n: middle_rectangle_method(  # noqa: E731
        integral_function, start, end, n
    )

    acc = float(input("Введите точность вычисления: "))
    three_eights_method_n = find_n(three_eights_method_findn, acc)
    middle_rectangle_method_n = find_n(middle_rectangle_method_findn, acc)
    print(f"3/8: {three_eights_method_n}, middle: {middle_rectangle_method_n}")


if __name__ == "__main__":
    main()
