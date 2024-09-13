# Implementar una versión con recursión de cola que produzca el resultado esperado al pasar una lista: `suma_resta_alternada([1, 2, 3, 4, 5]) = 1 + 2 - 3 + 4 - 5


def suma_resta_alternada(lista):
    def suma_resta_alternada_interna(lista, acumulador=None, signo=1):
        if len(lista) == 0 and acumulador is None:
            raise ValueError("La lista no puede ser vacia")
        if len(lista) == 0:
            return acumulador
        if acumulador is None:
            acumulador = lista[0]
            return suma_resta_alternada_interna(lista[1:], acumulador, signo)
        if signo == 1:
            return suma_resta_alternada_interna(lista[1:], acumulador + lista[0], -1)
        if signo == -1:
            return suma_resta_alternada_interna(lista[1:], acumulador - lista[0], 1)

    return suma_resta_alternada_interna(lista)


print(suma_resta_alternada([1, 2, 3, 4, 5]))  # 1 + 2 - 3 + 4 - 5 = -1)
