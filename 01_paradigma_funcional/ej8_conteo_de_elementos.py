from typing import Dict, List
from functools import reduce


def contar_elementos(lista: List[str]) -> Dict[str, int]:
    def contador(acumulado: Dict[str, int], elemento: str) -> Dict[str, int]:
        if elemento in acumulado:
            acumulado[elemento] += 1
        else:
            acumulado[elemento] = 1
        return acumulado

    return reduce(contador, lista, {})


if __name__ == "__main__":
    lista_de_cadenas = ["a", "b", "c", "a", "a", "c", "b", "d", "c", "a", "e"]
    print(contar_elementos(lista_de_cadenas))
