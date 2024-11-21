arr = map(int, input("Введите масисв: "))


class Solution(object):
    def __init__(self, arr):
        self.arr = arr

    def is_prime(n):
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        return d * d > n

    def new_array(arr: list) -> list:
        for el in len(range(arr)):
            if Solution.is_prime(arr[el]):
                for i in range(el, len(arr) - 1):
                    arr[i] = arr[i + 1]
        return arr

    def output(arr):
        arr[::-1]
        print(arr)


Solution.new_array(arr)
Solution.output(arr)
