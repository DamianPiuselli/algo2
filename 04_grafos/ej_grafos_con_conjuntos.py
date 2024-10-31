from typing import TypeVar, Generic, Set, Tuple, List, Optional

T = TypeVar("T")

# Grafo representando las aristas como conjuntos, no dirigido.


class Grafo(Generic[T]):
    def __init__(
        self,
        vertices: Optional[Set[T]] = None,
        aristas: Optional[Set[Tuple[T, T]]] = None,
    ) -> None:
        self.vertices = (
            vertices if vertices else set()
        )  # Conjunto de vértices o nodos del grafo

        self.aristas = (
            aristas if aristas else set()
        )  # Conjunto de aristas, que son pares de vértices

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

    def dfs(self) -> List[T]:
        visitados = set()  # almaceno los nodos visitados
        recorrido = []

        def dfs_recursivo(nodo):
            visitados.add(nodo)
            recorrido.append(nodo)

            # Recorrer los vecinos del nodo actual recursivamente con recursion de cola
            # la condicion al recorrer vecinos es que estos no hayan sido visitados
            for vecino in self.vecinos_de(nodo):
                if vecino not in visitados:
                    dfs_recursivo(vecino)

            # si el grafo no es conexo.
            if len(visitados) < len(self.vertices):
                for vertice in self.vertices:
                    if vertice not in visitados:
                        dfs_recursivo(vertice)

        if len(self.vertices) > 0:
            dfs_recursivo(next(iter(self.vertices)))

        return recorrido

    def bfs(self) -> List[T]:
        visitados = set()
        recorrido = []

        # cola para almacenar los nodos a visitar
        cola = []

        # agrego a la cola los nodos que no han sido visitados. Me permite extender bfs a grafos no conexos.
        for vertice in self.vertices:
            if vertice not in visitados:
                cola.append(vertice)

                while cola:
                    nodo = cola.pop(0)
                    visitados.add(nodo)
                    recorrido.append(nodo)

                    for vecino in self.vecinos_de(nodo):
                        if vecino not in visitados:
                            cola.append(vecino)

        return recorrido


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

    # test DFS en grafo no dirigido y conexo.
    grafo2 = Grafo()

    # Add nodes
    grafo2.agregar_nodo("A")
    grafo2.agregar_nodo("B")
    grafo2.agregar_nodo("C")
    grafo2.agregar_nodo("D")
    grafo2.agregar_nodo("E")
    grafo2.agregar_nodo("F")

    grafo2.agregar_arista("A", "B")
    grafo2.agregar_arista("A", "C")
    grafo2.agregar_arista("B", "D")
    grafo2.agregar_arista("B", "E")
    grafo2.agregar_arista("C", "F")

    print(grafo2)

    print(f"recorrido DFS: {grafo2.dfs()}")
    print(f"recorrido BFS: {grafo2.bfs()}")


if __name__ == "__main__":
    main()
