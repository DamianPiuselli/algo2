from typing import List
from functools import reduce


def insertar_en_orden(lista: List[int], numero: int) -> List[int]:
    for i, valor in enumerate(lista):
        if numero < valor:
            return lista[:i] + [numero] + lista[i:]
    return lista + [numero]


##insertar_en_orden debe tomar dos valores, el acumulador y el elemento actual.
## debe retornar el mismo tipo que el acumulador.


def ordenar_con_reduce(lista: List[int]) -> List[int]:
    return reduce(insertar_en_orden, lista, [])


if __name__ == "__main__":
    lista = [5, 3, 8, 1, 2, 7]
    resultado = ordenar_con_reduce(lista)
    print(resultado)
