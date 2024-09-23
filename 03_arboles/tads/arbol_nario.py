from typing import Generic, TypeVar, Optional
from functools import reduce

T = TypeVar("T")


class ArbolN(Generic[T]):
    def __init__(self, dato: T):
        self._dato: T = dato
        self._subarboles: list[ArbolN[T]] = []

    @property
    def dato(self) -> T:
        return self._dato

    @dato.setter
    def dato(self, valor: T):
        self._dato = valor

    @property
    def subarboles(self) -> "list[ArbolN[T]]":
        return self._subarboles

    @subarboles.setter
    def subarboles(self, subarboles: "list[ArbolN[T]]"):
        self._subarboles = subarboles

    def insertar_subarbol(self, subarbol: "ArbolN[T]"):
        self.subarboles.append(subarbol)

    def es_hoja(self) -> bool:
        return self.subarboles == []

    def altura(self) -> int:
        def altura_n(bosque: list[ArbolN[T]]) -> int:
            if not bosque:
                return 0
            else:
                return max(bosque[0].altura(), altura_n(bosque[1:]))

        return 1 + altura_n(self.subarboles)

    def __len__(self) -> int:
        if self.es_hoja():
            return 1
        else:
            return 1 + sum([len(subarbol) for subarbol in self.subarboles])

    def __str__(self):
        def mostrar(t: ArbolN[T], nivel: int):
            tab = "." * 4
            indent = tab * nivel
            out = indent + str(t.dato) + "\n"
            for subarbol in t.subarboles:
                out += mostrar(subarbol, nivel + 1)
            return out

        return mostrar(self, 0)

    def preorder(self) -> list[T]:
        return reduce(
            lambda recorrido, subarbol: recorrido + subarbol.preorder(),
            self.subarboles,
            [self.dato],
        )

    def preorder2(self) -> list[T]:
        recorrido = [self.dato]
        for subarbol in self.subarboles:
            recorrido += subarbol.preorder2()
        return recorrido

    def preorder3(self) -> list[T]:
        def preorder_n(bosque: list[ArbolN[T]]) -> list[T]:
            return [] if not bosque else bosque[0].preorder3() + preorder_n(bosque[1:])

        return [self.dato] + preorder_n(self.subarboles)

    def __eq__(self, otro: "ArbolN[T]") -> bool:
        if self.es_hoja() and otro.es_hoja():
            return self.dato == otro.dato

        if self.dato != otro.dato or len(self.subarboles) != len(otro.subarboles):
            return False

        return all(sub1 == sub2 for sub1, sub2 in zip(self.subarboles, otro.subarboles))

    def bfs(self) -> list[T]:
        cola = [self]
        recorrido = []
        while cola:
            nodo = cola.pop(0)
            recorrido.append(nodo.dato)
            if nodo.subarboles:
                cola.extend(nodo.subarboles)  # type: ignore
        return recorrido

    def posorder(self) -> list[T]:
        return reduce(
            lambda recorrido, subarbol: recorrido + subarbol.posorder(),
            self.subarboles,
            [],
        ) + [self.dato]

    def posorder2(self) -> list[T]:  # recursion mutua
        def posorder_n(bosque: list[ArbolN[T]]) -> list[T]:
            if not bosque:
                return []
            else:
                return bosque[0].posorder2() + posorder_n(bosque[1:])

        return posorder_n(self.subarboles) + [self.dato]

    def nivel(self, x: T) -> int:
        if self.dato == x:
            return 1
        else:
            for subarbol in self.subarboles:
                nivel_subarbol = subarbol.nivel(x)
                if nivel_subarbol != -1:
                    return 1 + nivel_subarbol
        return -1

    def copy(self) -> "ArbolN[T]":
        if self.es_hoja():
            return ArbolN(self.dato)
        else:
            new_tree = ArbolN(self.dato)
            new_tree.subarboles = [subarbol.copy() for subarbol in self.subarboles]
            return new_tree

    def sin_hojas(self) -> "ArbolN[T]":
        new_tree = ArbolN(self.dato)
        new_tree.subarboles = [
            subarbol.sin_hojas()
            for subarbol in self.subarboles
            if not subarbol.es_hoja()
        ]
        return new_tree

    def recorrido_guiado(self, direcciones: list[int]) -> Optional[T]:
        if direcciones == []:
            return self.dato
        else:
            direccion = direcciones.pop(0)
            if direccion < len(self.subarboles):
                return self.subarboles[direccion].recorrido_guiado(direcciones)
            else:
                return None


def main():
    t = ArbolN(1)
    n2 = ArbolN(2)
    n3 = ArbolN(3)
    n4 = ArbolN(4)
    n5 = ArbolN(5)
    n6 = ArbolN(6)
    n7 = ArbolN(7)
    n8 = ArbolN(8)
    n9 = ArbolN(9)
    t.insertar_subarbol(n2)
    t.insertar_subarbol(n3)
    t.insertar_subarbol(n4)
    n2.insertar_subarbol(n5)
    n2.insertar_subarbol(n6)
    n4.insertar_subarbol(n7)
    n4.insertar_subarbol(n8)
    n7.insertar_subarbol(n9)

    print(t)

    print(f"Altura: {t.altura()}")
    print(f"Nodos: {len(t)}")

    print(f"BFS: {t.bfs()}")
    print(f"DFS preorder : {t.preorder()}")
    print(f"DFS preorder2: {t.preorder2()}")
    print(f"DFS preorder3: {t.preorder3()}")
    print(f"DFS posorder: {t.posorder()}")
    print(f"DFS posorder recursion mutua: {t.posorder2()}")

    print(f"Nivel de 9: {t.nivel(9)}")
    print(f"Nivel de 13: {t.nivel(13)}")

    t2 = t.copy()
    t3 = t2.sin_hojas()
    print(t)
    print(t2)
    print(t3)
    print(f"t == t2 {t == t2}")

    print(f"recorrido_guiado [2,0,0]: {t2.recorrido_guiado([2,0,0])}")
    print(f"recorrido_guiado [2,0,1]: {t2.recorrido_guiado([2,0,1])}")


if __name__ == "__main__":
    main()
