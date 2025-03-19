def decimal_to_binary(number):
    integer_part = int(number)
    fractional_part = number - integer_part

    binary_integer = ""
    if integer_part == 0:
        binary_integer = "0"
    while integer_part > 0:
        binary_integer = str(integer_part % 2) + binary_integer
        integer_part //= 2

    binary_fraction = ""
    count = 0
    while fractional_part and count < 10:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fraction += str(bit)
        fractional_part -= bit
        count += 1

    return binary_integer + ("." + binary_fraction if binary_fraction else "")


def binary_to_decimal(binary_str):
    if "." in binary_str:
        integer_part, fractional_part = binary_str.split(".")
    else:
        integer_part, fractional_part = binary_str, ""

    decimal_integer = 0
    power = 1
    for digit in reversed(integer_part):
        decimal_integer += int(digit) * power
        power *= 2

    decimal_fraction = 0
    power = 0.5
    for digit in fractional_part:
        decimal_fraction += int(digit) * power
        power /= 2

    return decimal_integer + decimal_fraction
