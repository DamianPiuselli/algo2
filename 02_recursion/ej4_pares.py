from typing import List, Tuple


def pares(n: int, i: int = 1) -> List[Tuple[int, int]]:

    j = n - i  # complemento
    if i >= j:
        return []
    else:
        return [(i, j)] + pares(n, i + 1)


if __name__ == "__main__":
    print(pares(61))
