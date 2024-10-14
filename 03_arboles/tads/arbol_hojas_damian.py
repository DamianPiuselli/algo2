from typing import Generic, TypeVar

T = TypeVar("T")  # tipo de dato de las hojas
S = TypeVar("S")  # tipo de dato de los nodos


class ArbolH(Generic[T, S]):
    # el constructor crea una Hoja, idealmente solo aceptaria parametros de tipo T,
    # pero no se puede por limitaciones del lenguaje.

    def __init__(self, dato: T | S):
        self._dato: T | S = dato
        self._subarboles: list[ArbolH[T, S]] = []
        self._tipo_hoja = type(dato)
        self._tipo_nodo = None

    # La creación de un árbol con un nodo intermedio y una o más hojas podría implementarse con un método constructor estático.
    @staticmethod
    def crear_nodo_y_hojas(dato_raiz: S, *datos_hojas: T) -> "ArbolH[T, S]":
        if not datos_hojas:
            raise ValueError("Se requiere al menos un dato para las hojas")
        if not all([isinstance(dato, type(datos_hojas[0])) for dato in datos_hojas]):
            raise ValueError("Todos los datos de las hojas deben ser del mismo tipo")

        nuevo = ArbolH(dato_raiz)
        for dato in datos_hojas:
            subarbol = ArbolH(dato)
            subarbol._tipo_nodo = type(dato_raiz)
            nuevo._subarboles.append(subarbol)
        nuevo._tipo_nodo = type(dato_raiz)
        nuevo._tipo_hoja = type(datos_hojas[0])
        return nuevo

    def insertar_subarbol(self, subarbol: "ArbolH[T,S]"):
        if self.es_hoja():
            raise ValueError("No se pueden insertar subárboles en un nodo hoja")

        if not self._son_mismos_tipos(subarbol):
            raise ValueError(
                "El árbol a insertar no es consistente con los tipos de datos del árbol actual"
            )

        subarbol._tipo_nodo = self._tipo_nodo
        self.subarboles.append(subarbol)

    def _son_mismos_tipos(self, otro: "ArbolH[T,S]") -> bool:
        return (
            isinstance(otro, ArbolH)
            and (self._tipo_nodo == otro._tipo_nodo or self.es_hoja() or otro.es_hoja())
            and self._tipo_hoja == otro._tipo_hoja
        )

    def es_hoja(self) -> bool:
        return self.subarboles == []

    @property
    def subarboles(self) -> "list[ArbolH[T,S]]":
        return self._subarboles

    def __str__(self) -> str:
        def mostrar(t: ArbolH[T, S], nivel: int):
            tab = "." * 4
            indent = tab * nivel
            if t.es_hoja():
                dato = f"[{t.dato_hoja()}]"
            else:
                dato = str(t.dato_nodo())
            out = f"{indent} {dato} \n"
            for subarbol in t.subarboles:
                out += mostrar(subarbol, nivel + 1)
            return out

        return mostrar(self, 0)

    def dato_hoja(self) -> T:
        if self.es_hoja():
            return self._dato
        raise ValueError("El nodo actual no es una hoja")

    def dato_nodo(self) -> S:
        if not self.es_hoja():
            return self._dato
        raise ValueError("El nodo actual es una hoja")

    def es_valido(self) -> bool:
        if self.es_hoja():
            return True

        # Verificamos si los tipos de los subárboles son consistentes
        for subarbol in self._subarboles:
            # Verificamos que los nodos hoja tengan el mismo tipo
            if subarbol.es_hoja() and type(subarbol._dato) != self._tipo_hoja:
                return False

            # Verificamos que los nodos intermedios tengan el mismo tipo
            if not subarbol.es_hoja() and type(subarbol._dato) != self._tipo_nodo:
                return False

            # Validamos el subárbol recursivamente
            if not subarbol.es_valido():
                return False

        return True


def main():
    nodo_b = ArbolH.crear_nodo_y_hojas("b", 6, 7)
    nodo_c = ArbolH.crear_nodo_y_hojas("c", 8, 9)
    arbol = ArbolH.crear_nodo_y_hojas("a", 1, 2, 3, 4, 5)

    print(arbol._tipo_hoja, arbol._tipo_nodo)
    print(nodo_b._tipo_hoja, nodo_b._tipo_nodo)
    print(nodo_c._tipo_hoja, nodo_c._tipo_nodo)

    arbol.insertar_subarbol(nodo_b)
    nodo_b.insertar_subarbol(nodo_c)
    nodo_c.insertar_subarbol(ArbolH(10))

    print(arbol)
    print(arbol._tipo_hoja, arbol._tipo_nodo)
    print(nodo_b._tipo_hoja, nodo_b._tipo_nodo)
    print(nodo_c._tipo_hoja, nodo_c._tipo_nodo)

    nodo_int = ArbolH.crear_nodo_y_hojas(1, 2, 3)
    # arbol.insertar_subarbol(nodo_int)  # Debería lanzar una excepción

    print(arbol.es_valido())
    # CAMBIO el arbol para que no sea mas valido (diferentes tipos para las hojas y los nodos)
    # No uso insertar para saltearme la validacion de datos y poder generar un arbol invalido.
    arbol.subarboles[0] = ArbolH.crear_nodo_y_hojas(2, "asd", "asddd")
    print(arbol.es_valido())


if __name__ == "__main__":
    main()
