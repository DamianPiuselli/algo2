from typing import Tuple, Dict, Set, TypeVar, Generic, List

T = TypeVar("T")


class GrafoConjuntos(Generic[T]):
    def __init__(self):
        self.nodos: Set[T] = set()
        self.aristas: Dict[Tuple[T, T], int] = {}

    def agregar_nodo(self, nodo: T) -> None:
        if nodo in self.nodos:
            raise ValueError("El nodo ya existe en el grafo")
        else:
            self.nodos.add(nodo)

    def agregar_arista(self, origen: T, destino: T, peso: int) -> None:
        if not (origen in self.nodos and destino in self.nodos):
            raise ValueError("Ambos nodos deben existir en el grafo")
        else:
            self.aristas[(origen, destino)] = peso

    def __str__(self) -> str:
        return f"\nVertices: {self.nodos}\nAristas: {self.aristas}\n"

    def vecino_de(self, nodo: T) -> Set[T]:
        vecinos = set()
        for (origen, destino), peso in self.aristas.items():
            if origen == nodo:
                vecinos.add(destino)
        return vecinos

    def dijkstra_recursivo(self, inicio: T, destino: T) -> List[T]:

        # etiquetas
        etiquetas = {nodo: (None, float("inf")) for nodo in self.nodos}
        etiquetas[inicio] = (None, 0)

        # los nodos a visitar van en una cola
        cola = []
        cola.append(inicio)

        # el proceso de actualizar las etiquetas termina cuando se vacia la cola
        # OBS: no pueden existir ciclos negativos
        while cola:
            actual = cola.pop(0)
            # itero sobre los posibles nodos a los que puedo viajar desde actual
            for vecino in self.vecino_de(actual):
                peso = self.aristas[(actual, vecino)]
                if peso + etiquetas[actual][1] < etiquetas[vecino][1]:
                    etiquetas[vecino] = (actual, peso + etiquetas[actual][1])
                    cola.append(vecino)

        # armo el camino
        camino = []
        actual = destino
        while actual:
            camino.insert(0, actual)
            actual = etiquetas[actual][0]

        return camino


def main():
    grafo = GrafoConjuntos[str]()
    grafo.agregar_nodo("a")
    grafo.agregar_nodo("b")
    grafo.agregar_nodo("c")
    grafo.agregar_nodo("d")
    grafo.agregar_nodo("e")
    grafo.agregar_nodo("f")
    grafo.agregar_nodo("g")

    grafo.agregar_arista("a", "b", 4)
    grafo.agregar_arista("a", "c", 2)
    grafo.agregar_arista("a", "d", 3)
    grafo.agregar_arista("c", "b", 1)
    grafo.agregar_arista("b", "g", 3)
    grafo.agregar_arista("b", "e", 1)
    grafo.agregar_arista("d", "e", -2)
    grafo.agregar_arista("e", "f", -1)
    grafo.agregar_arista("f", "b", 2)

    print(grafo)
    print(f"camino minimo dijkstra optimizado: {grafo.dijkstra_recursivo('a', 'f')}")


if __name__ == "__main__":
    main()
