from typing import Tuple, Dict, Set, TypeVar, Generic, List

T = TypeVar("T")


class GrafoBellmanFord(Generic[T]):
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

    def bellman_ford(self, inicio: T, destino: T) -> List[T]:
        # Inicializo las etiquetas de los nodos
        etiquetas = {nodo: (None, float("inf")) for nodo in self.nodos}
        etiquetas[inicio] = (None, 0)

        # itero |V| - 1 veces
        for _ in range(len(self.nodos) - 1):
            cambios_durante_iteracion = False
            for (origen, destino), peso in self.aristas.items():
                if etiquetas[origen][1] + peso < etiquetas[destino][1]:
                    cambios_durante_iteracion = True
                    etiquetas[destino] = (origen, etiquetas[origen][1] + peso)  # type: ignore
            if not cambios_durante_iteracion:
                break

        # Verifico si hay ciclos negativos (no deberia haber cambios en la ultima iteracion)
        for (origen, destino), peso in self.aristas.items():
            if etiquetas[origen][1] + peso < etiquetas[destino][1]:
                raise ValueError("El grafo contiene un ciclo negativo")

        # Reconstruyo el camino

        camino = []
        actual = destino
        while actual:
            camino.insert(0, actual)
            actual = etiquetas[actual][0]

        return camino


def main():
    grafo = GrafoBellmanFord[str]()
    grafo.agregar_nodo("a")
    grafo.agregar_nodo("b")
    grafo.agregar_nodo("d")
    grafo.agregar_nodo("e")
    grafo.agregar_nodo("f")

    grafo.agregar_arista("a", "b", 5)
    grafo.agregar_arista("a", "d", 3)
    grafo.agregar_arista("d", "e", 2)
    grafo.agregar_arista("e", "f", 1)
    grafo.agregar_arista("e", "b", 1)
    grafo.agregar_arista("b", "f", -1)

    print(grafo)
    print(f"camino minimo bellman ford: {grafo.bellman_ford('a', 'f')}")


if __name__ == "__main__":
    main()
