from typing import Generic, TypeVar, Optional, List

T = TypeVar("T")


class GrafoConjuntos(Generic[T]):
    def __init__(self):
        self.nodos: set[T] = set()
        self.aristas: dict[tuple[T, T], int] = {}

    def agregar_nodo(self, nodo: T):
        self.nodos.add(nodo)

    def agregar_arista(self, origen: T, destino: T, peso: int):
        if origen in self.nodos and destino in self.nodos:
            if isinstance(peso, int) and peso > 0:
                self.aristas[(origen, destino)] = peso
            else:
                raise ValueError("El peso de la arista debe ser un entero positivo")

    def eliminar_nodo(self, nodo: T):
        self.nodos.discard(nodo)
        aristas_sin_nodo = {
            (origen, destino): peso
            for (origen, destino), peso in self.aristas.items()
            if origen != nodo and destino != nodo
        }
        self.aristas = aristas_sin_nodo

    def eliminar_arista(self, origen: T, destino: T):
        self.aristas.pop((origen, destino), None)

    def es_vecino_de(self, origen: T, destino: T) -> bool:
        return (origen, destino) in self.aristas or (destino, origen) in self.aristas

    def vecinos_de(self, nodo: T) -> set[T]:
        vecinos = set()
        for (origen, destino), peso in self.aristas.items():
            if origen == nodo:
                vecinos.add(destino)
            elif destino == nodo:
                vecinos.add(origen)
        return vecinos

    def peso_arista(self, origen: T, destino: T) -> Optional[int]:
        return self.aristas.get(
            (origen, destino), self.aristas.get((destino, origen), None)
        )

    def __str__(self) -> str:
        return f"\nVertices: {self.nodos}\nAristas: {self.aristas}\n"

    def dijkstra_recursivo(self, inicio: T, destino: T) -> List[T]:
        visitados = set()
        etiquetas = {nodo: (None, float("inf")) for nodo in self.nodos}
        etiquetas[inicio] = (None, 0)

        def dijkstra_recursivo_aux(nodo_actual: T):
            visitados.add(nodo_actual)
            for vecino in self.vecinos_de(nodo_actual):
                if vecino not in visitados:
                    peso_arista = self.peso_arista(nodo_actual, vecino)
                    peso_total = etiquetas[nodo_actual][1] + peso_arista
                    if peso_total < etiquetas[vecino][1]:
                        etiquetas[vecino] = (nodo_actual, peso_total)

            if len(visitados) < len(self.nodos):
                nodo_menor_peso = None
                menor_peso = float("inf")

                for nodo, (predecesor, peso) in etiquetas.items():
                    if nodo not in visitados and peso < menor_peso:
                        nodo_menor_peso = nodo
                        menor_peso = peso

                dijkstra_recursivo_aux(nodo_menor_peso)

        dijkstra_recursivo_aux(inicio)

        # construir el camino entre inicio y fin con las etiquetas
        camino = []
        nodo_actual = destino
        while nodo_actual is not None:
            camino.append(nodo_actual)
            nodo_actual = etiquetas[nodo_actual][0]

        return camino


def main():
    grafo = GrafoConjuntos[str]()
    grafo.agregar_nodo("a")
    grafo.agregar_nodo("b")
    grafo.agregar_nodo("c")
    grafo.agregar_nodo("d")
    grafo.agregar_nodo("e")
    grafo.agregar_nodo("f")
    grafo.agregar_arista("a", "b", 5)
    grafo.agregar_arista("a", "c", 2)
    grafo.agregar_arista("a", "d", 3)
    grafo.agregar_arista("b", "c", 1)
    grafo.agregar_arista("b", "e", 1)
    grafo.agregar_arista("b", "f", 3)
    grafo.agregar_arista("d", "e", 2)
    grafo.agregar_arista("e", "f", 1)
    print(grafo)
    print(f"camino minimo dijkstra: {grafo.dijkstra_recursivo('a', 'f')}")


if __name__ == "__main__":
    main()
