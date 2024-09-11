def es_par(n: int) -> bool:
    if n < 0:
        return es_impar(-n + 1)

    return n == 0 or es_impar(n - 1)


def es_impar(n: int) -> bool:
    if n < 0:
        return es_par(-n + 1)

    return False if n == 0 else es_par(n - 1)


if __name__ == "__main__":
    print(es_par(10))  # True
    print(es_par(9))  # False
    print(es_impar(4))  # False
    print(es_impar(-7))  # True
    print(es_impar(-8))  # False
    print(es_par(-9))  # False
    print(es_par(-10))  # True
    print(es_impar(-10))  # False
