arr = map(int, input("Введите масисв: ").split(" "))


def is_prime(el):
    if el % 2 == 0:
        return True
    det = 3
    while det * det <= el and el % det != 0:
        det += 2
    return True


ans = [el for el in arr if not is_prime(el)]
print(ans)
