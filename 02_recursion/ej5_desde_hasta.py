from typing import List
from functools import reduce


def desde_hasta(i: int, f: int) -> List[int]:
    if i > f:
        raise ValueError("El primer argumento debe ser menor o igual al segundo")

    if i == f:
        return [f]

    return [i] + desde_hasta(i + 1, f)


def sumatoria(n: int) -> int:
    return sum(desde_hasta(1, n))


def factorial(n: int) -> int:
    return reduce(lambda x, y: x * y, desde_hasta(1, n), 1)


if __name__ == "__main__":
    print(desde_hasta(1, 5))
    print(sumatoria(5))
    print(factorial(5))
