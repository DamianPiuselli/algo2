def resta_lista(xs: list[int]) -> int:
    def apilado(xs: list[int], pila: list[int]):
        if xs != []:
            pila.append(xs[0])
            apilado(xs[1:], pila)

    def desapilado(pila: list[int], acumulador: int) -> int:
        if pila == []:
            return acumulador
        else:
            return desapilado(pila, pila.pop() - acumulador)

    pila: list = []
    apilado(xs, pila)
    return desapilado(pila, 0)


def resta_pila_iterativa(xs: list[int]) -> int:
    pila: list = []
    for x in xs:
        pila.append(x)

    acumulador: int = 0
    while pila != []:
        acumulador = pila.pop() - acumulador

    return acumulador


print(resta_lista([10, 2, 5, 9]))  # (10 - (2 - (5 - 9))
print(resta_pila_iterativa([10, 2, 5, 9]))  # (10 - (2 - (5 - 9))
