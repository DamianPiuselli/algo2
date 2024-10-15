from typing import TypeVar, Generic, Dict, Set, Tuple

T = TypeVar("T")

# Grafo con listas de adyacencia ponderado, no dirigido.


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
        # adyacencia se modela como un set de tuplas (nodo, peso)
        self.nodos: Dict[Nodo[T], Set[Tuple[Nodo[T], float]]] = {}

    def agregar_nodo(self, nodo: Nodo[T]) -> None:
        if nodo not in self.nodos:
            self.nodos[nodo] = set()

    def agregar_arista(self, desde: Nodo[T], hacia: Nodo[T], peso: float) -> None:
        if not (desde in self.nodos and hacia in self.nodos):
            raise ValueError("Ambos nodos deben existir en el grafo")

        if any(nodo == desde for nodo, peso in self.nodos[hacia]) or any(
            nodo == hacia for nodo, peso in self.nodos[desde]
        ):
            raise ValueError("La arista ya existe en el grafo")

        else:
            self.nodos[desde].add((hacia, peso))
            self.nodos[hacia].add((desde, peso))


def main():
    nodo1 = Nodo("A")
    nodo2 = Nodo("B")
    nodo3 = Nodo("C")
    grafo = Grafo()

    grafo.agregar_nodo(nodo1)
    grafo.agregar_nodo(nodo2)
    grafo.agregar_nodo(nodo3)
    grafo.agregar_arista(nodo1, nodo2, 3.5)
    grafo.agregar_arista(nodo1, nodo3, 4.5)
    # grafo.agregar_arista(nodo1, nodo3, 2.5)  # Agregar esta linea genera un ValueError

    print(grafo.nodos)


if __name__ == "__main__":
    main()
