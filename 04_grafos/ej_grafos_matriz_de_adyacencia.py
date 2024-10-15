from typing import TypeVar, Generic, Dict, Set, Tuple, List

T = TypeVar("T")

# Grafo con matriz de adyacencia, no dirigido.


class Nodo(Generic[T]):
    def __init__(self, dato: T) -> None:
        self.dato = dato

    def __hash__(self):
        return hash(self.dato)

    def __eq__(self, otro):
        if isinstance(otro, Nodo):
            return self.dato == otro.dato
        return False

    def __repr__(self):
        return str(self.dato)


class Grafo(Generic[T]):
    def __init__(self) -> None:
        self.nodos: List[Nodo[T]] = []
        self.adyacencias: List[List[int]] = []

    def agregar_nodo(self, nodo: Nodo[T]) -> None:
        if nodo in self.nodos:
            raise ValueError("El nodo ya existe en el grafo")
        else:
            self.nodos.append(nodo)

            for fila in self.adyacencias:
                fila.append(0)
            self.adyacencias.append([0] * len(self.nodos))

    def agregar_arista(self, desde: Nodo[T], hacia: Nodo[T]) -> None:
        if not (desde in self.nodos and hacia in self.nodos):
            raise ValueError("Ambos nodos deben existir en el grafo")

        # asigno 1 en lugar de sumar 1, por lo cual si la coneccion ya existe no se va a modificar
        desde_idx = self.nodos.index(desde)
        hacia_idx = self.nodos.index(hacia)
        self.adyacencias[desde_idx][hacia_idx] = 1
        self.adyacencias[hacia_idx][desde_idx] = 1

    def eliminar_nodo(self, nodo: Nodo[T]) -> None:
        if nodo not in self.nodos:
            raise ValueError("El nodo no existe en el grafo")
        else:
            nodo_idx = self.nodos.index(nodo)
            self.nodos.pop(nodo_idx)
            # elimino la i-esima lista
            self.adyacencias.pop(nodo_idx)
            # elimino el i-esimo elemento de cada lista restante
            for fila in self.adyacencias:
                fila.pop(nodo_idx)

    def eliminar_arista(self, desde: Nodo[T], hacia: Nodo[T]) -> None:
        if not (desde in self.nodos and hacia in self.nodos):
            raise ValueError("Ambos nodos deben existir en el grafo")

        desde_idx = self.nodos.index(desde)
        hacia_idx = self.nodos.index(hacia)
        self.adyacencias[desde_idx][hacia_idx] = 0
        self.adyacencias[hacia_idx][desde_idx] = 0

    def existe_conexion(self, desde: Nodo[T], hacia: Nodo[T]) -> bool:
        if not (desde in self.nodos and hacia in self.nodos):
            raise ValueError("Ambos nodos deben existir en el grafo")

        desde_idx = self.nodos.index(desde)
        hacia_idx = self.nodos.index(hacia)
        return self.adyacencias[desde_idx][hacia_idx] == 1

    def ver_conexion(self, desde: Nodo[T], hacia: Nodo[T]) -> str:
        if not (desde in self.nodos and hacia in self.nodos):
            raise ValueError("Ambos nodos deben existir en el grafo")

        if self.existe_conexion(desde, hacia):
            desde_idx = self.nodos.index(desde)
            hacia_idx = self.nodos.index(hacia)
            return f"La conexion entre {desde} y {hacia} es de {self.adyacencias[desde_idx][hacia_idx]}"
        else:
            return f"No existe conexion entre {desde} y {hacia}"

    def es_vecino(self, nodo1: Nodo[T], nodo2: Nodo[T]) -> bool:
        return self.existe_conexion(nodo1, nodo2)

    def vecinos(self, nodo: Nodo[T]) -> List[Nodo[T]]:
        if nodo not in self.nodos:
            raise ValueError("El nodo no existe en el grafo")
        else:
            nodo_idx = self.nodos.index(nodo)
            return [
                self.nodos[i]
                for i, ady in enumerate(self.adyacencias[nodo_idx])
                if ady == 1
            ]

    def __str__(self):
        nodos_str = str(self.nodos)
        ady_str = "\n".join(str(fila) for fila in self.adyacencias)
        return nodos_str + "\n" + "-" * len(nodos_str) + "\n" + ady_str + "\n"

    def es_completo(self) -> bool:
        for i in range(len(self.nodos)):
            for j in range(len(self.nodos)):
                if i != j and self.adyacencias[i][j] == 0:
                    return False
        return True

    def es_bipartito(self) -> bool:
        pass


def main():
    nodo1 = Nodo("A")
    nodo2 = Nodo("B")
    nodo3 = Nodo("C")
    grafo = Grafo()

    grafo.agregar_nodo(nodo1)
    grafo.agregar_nodo(nodo2)
    grafo.agregar_nodo(nodo3)
    print(grafo)

    grafo.agregar_arista(nodo1, nodo1)
    grafo.agregar_arista(nodo1, nodo2)
    grafo.agregar_arista(nodo1, nodo3)
    print(grafo)

    print(f"existe conexion n1 y n1: {grafo.existe_conexion(nodo1, nodo1)}")
    print(f"existe conexion n1 y n2: {grafo.existe_conexion(nodo1, nodo3)}")
    print(grafo.ver_conexion(nodo1, nodo1))
    print(grafo.ver_conexion(nodo1, nodo3))

    print(f"nodo1 y nodo2 son vecinos: {grafo.es_vecino(nodo1, nodo2)}")
    print(f"nodo1 y nodo3 son vecinos: {grafo.es_vecino(nodo1, nodo3)}")

    print(f"vecinos de nodo1: {grafo.vecinos(nodo1)}")
    print(f"vecinos de nodo3: {grafo.vecinos(nodo3)}")

    print(f"es completo {grafo.es_completo()}")

    grafo.eliminar_nodo(nodo2)
    print(grafo)

    grafo.eliminar_arista(nodo1, nodo3)
    print(grafo)


if __name__ == "__main__":
    main()
