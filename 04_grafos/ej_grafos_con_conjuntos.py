from typing import TypeVar, Generic, Set, Tuple, List

T = TypeVar("T")

# Grafo representando las aristas como conjuntos, no dirigido.


class Grafo(Generic[T]):
    def __init__(
        self, vertices: Set[T] = set(), aristas: Set[Tuple[T, T]] = set()
    ) -> None:
        self.vertices = vertices  # Conjunto de vértices o nodos del grafo
        self.aristas = aristas  # Conjunto de aristas, que son pares de vértices

    def agregar_nodo(self, nodo: T) -> None:
        if nodo in self.vertices:
            raise ValueError("El nodo ya existe en el grafo")
        else:
            self.vertices.add(nodo)

    def agregar_arista(self, origen: T, destino: T) -> None:
        if not (origen in self.vertices and destino in self.vertices):
            raise ValueError("Ambos nodos deben existir en el grafo")
        else:
            self.aristas.add((origen, destino))
            self.aristas.add((destino, origen))

    def eliminar_arista(self, origen: T, destino: T) -> None:
        if not (origen in self.vertices and destino in self.vertices):
            raise ValueError("Ambos nodos deben existir en el grafo")
        else:
            self.aristas.remove((origen, destino))
            self.aristas.remove((destino, origen))

    def eliminar_nodo(self, nodo: T) -> None:
        if nodo not in self.vertices:
            raise ValueError("El nodo no existe en el grafo")
        else:
            self.vertices.remove(nodo)
            # Eliminar aristas que tengan a nodo como origen o destino
            self.aristas = {arista for arista in self.aristas if nodo not in arista}

    def es_vecino_de(self, nodo: T, otro_nodo: T) -> bool:
        return (nodo, otro_nodo) in self.aristas or (otro_nodo, nodo) in self.aristas

    def vecinos_de(self, nodo: T) -> set[T]:
        return {vecino for vecino in self.vertices if self.es_vecino_de(nodo, vecino)}

    def __str__(self) -> str:
        return f"\nVertices: {self.vertices}\nAristas: {self.aristas}\n"


def main():
    grafo = Grafo()

    # Add nodes
    grafo.agregar_nodo("A")
    grafo.agregar_nodo("B")
    grafo.agregar_nodo("C")

    # Add edges
    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("A", "C")

    # Test eliminar_nodo
    print("Before removing node 'B':", grafo)
    grafo.eliminar_nodo("B")
    print("After removing node 'B':", grafo)

    # Test es_vecino_de
    print("Is 'A' a neighbor of 'C'?", grafo.es_vecino_de("A", "C"))
    print("Is 'A' a neighbor of 'B'?", grafo.es_vecino_de("A", "B"))

    # Test vecinos_de
    print("Neighbors of 'A':", grafo.vecinos_de("A"))
    print("Neighbors of 'B':", grafo.vecinos_de("B"))


if __name__ == "__main__":
    main()
