from collections.abc import Callable
from typing import Any, Generic, Optional, TypeVar
from functools import wraps

T = TypeVar("T")


class NodoAB(Generic[T]):
    def __init__(
        self,
        dato: T,
        si: "Optional[ArbolBinario[T]]" = None,
        sd: "Optional[ArbolBinario[T]]" = None,
    ):
        self.dato = dato
        self.si: ArbolBinario[T] = ArbolBinario() if si is None else si
        self.sd: ArbolBinario[T] = ArbolBinario() if sd is None else sd

    def __str__(self):
        return self.dato


class ArbolBinario(Generic[T]):
    def __init__(self):
        self.raiz: Optional[NodoAB[T]] = None

    class _Decoradores:
        @classmethod
        def valida_es_vacio(cls, f: Callable[..., Any]) -> Callable[..., Any]:
            @wraps(f)
            def wrapper(self, *args: Any, **kwargs: Any) -> Any:
                if self.es_vacio():
                    raise TypeError("Arbol Vacio")
                return f(self, *args, **kwargs)

            return wrapper

    @staticmethod
    def crear_nodo(
        dato: T,
        si: "Optional[ArbolBinario[T]]" = None,
        sd: "Optional[ArbolBinario[T]]" = None,
    ) -> "ArbolBinario[T]":
        t = ArbolBinario()
        t.raiz = NodoAB(dato, si, sd)
        return t

    def es_vacio(self) -> bool:
        return self.raiz is None

    @_Decoradores.valida_es_vacio
    def si(self) -> "ArbolBinario[T]":
        assert self.raiz is not None
        return self.raiz.si

    @_Decoradores.valida_es_vacio
    def sd(self) -> "ArbolBinario[T]":
        assert self.raiz is not None
        return self.raiz.sd

    def es_hoja(self) -> bool:
        return not self.es_vacio() and self.si().es_vacio() and self.sd().es_vacio()

    @_Decoradores.valida_es_vacio
    def dato(self) -> T:
        assert self.raiz is not None
        return self.raiz.dato

    @_Decoradores.valida_es_vacio
    def insertar_si(self, si: "ArbolBinario[T]"):
        assert self.raiz is not None
        self.raiz.si = si

    @_Decoradores.valida_es_vacio
    def insertar_sd(self, sd: "ArbolBinario[T]"):
        assert self.raiz is not None
        self.raiz.sd = sd

    def set_raiz(self, nodo: NodoAB[T]):
        self.raiz = nodo

    def altura(self) -> int:
        if self.es_vacio():
            return 0
        else:
            return 1 + max(self.si().altura(), self.sd().altura())

    def __len__(self) -> int:
        if self.es_vacio():
            return 0
        else:
            return 1 + len(self.si()) + len(self.sd())

    def __str__(self):
        def mostrar(t: ArbolBinario[T], nivel: int):
            tab = "." * 4
            indent = tab * nivel
            if t.es_vacio():
                return indent + "AV\n"
            else:
                out = indent + str(t.dato()) + "\n"
                out += mostrar(t.si(), nivel + 1)
                out += mostrar(t.sd(), nivel + 1)
                return out

        return mostrar(self, 0)

    def inorder(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return self.si().inorder() + [self.dato()] + self.sd().inorder()

    # DFS inorder sin recursion de cola
    def inorder_tail(self) -> list[T]:
        stack = []
        out = []
        current = self
        while stack or current:
            if current:
                stack.append(current)
                current = current.si()
            else:
                current = stack.pop()
                out.append(current.dato())
                current = current.sd()
        return out

    def preorder(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return [self.dato()] + self.si().preorder() + self.sd().preorder()

    def posorder(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return self.si().posorder() + self.sd().posorder() + [self.dato()]

    def bfs(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            queue = [self]
            out = []
            while queue:
                t = queue.pop(0)
                out.append(t.dato())
                if not t.si().es_vacio():
                    queue.append(t.si())
                if not t.sd().es_vacio():
                    queue.append(t.sd())
            return out

    # given a value of a node, find the node with that value and return the level of the node. root node start as one.
    def nivel(self, x: T) -> int:
        if self.es_vacio():
            return 0
        if self.dato() == x:
            return 1
        else:
            return 1 + max(self.si().nivel(x), self.sd().nivel(x))

    def copy(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            return ArbolBinario()
        else:
            new_tree = ArbolBinario()
            new_tree.set_raiz(NodoAB(self.dato(), self.si().copy(), self.sd().copy()))
            return new_tree

    def espejo(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            return ArbolBinario()
        else:
            new_tree = ArbolBinario()
            new_tree.set_raiz(
                NodoAB(self.dato(), self.sd().espejo(), self.si().espejo())
            )
            return new_tree

    def sin_hojas(self) -> "ArbolBinario[T]":
        if self.es_vacio() or self.es_hoja():
            return ArbolBinario()
        else:
            new_tree = ArbolBinario()
            new_tree.set_raiz(
                NodoAB(self.dato(), self.si().sin_hojas(), self.sd().sin_hojas())
            )
            return new_tree

    def recorrido_guiado(self, recorrido: list[str]) -> Optional[T]:
        if self.raiz == None:
            return None
        if recorrido == []:
            return self.dato()
        else:
            if recorrido[0] == "izquierda":
                return self.si().recorrido_guiado(recorrido[1:])
            if recorrido[0] == "derecha":
                return self.sd().recorrido_guiado(recorrido[1:])
            else:
                raise ValueError("Recorrido no valido")


def main():
    t = ArbolBinario.crear_nodo(1)
    n2 = ArbolBinario.crear_nodo(2)
    n3 = ArbolBinario.crear_nodo(3)
    n4 = ArbolBinario.crear_nodo(4)
    n5 = ArbolBinario.crear_nodo(5)
    n6 = ArbolBinario.crear_nodo(6)
    n7 = ArbolBinario.crear_nodo(7)
    n8 = ArbolBinario.crear_nodo(8)
    n2.insertar_si(n4)
    n2.insertar_sd(n5)
    n5.insertar_si(n8)
    n3.insertar_si(n6)
    n3.insertar_sd(n7)
    t.insertar_si(n2)
    t.insertar_sd(n3)

    print(t)

    print(f"Altura: {t.altura()}")
    print(f"Nodos: {len(t)}")

    recorrido = ["izquierda", "derecha"]
    print(f"Recorrido_guidado{str(recorrido):<30}: {t.recorrido_guiado(recorrido)}")

    print(f"BFS: {t.bfs()}")

    t2 = t.copy()
    print(t2)
    print(f"Nivel de 8: {t2.nivel(8)}")
    print(f"DFS inorder stack: {t2.inorder()}")
    print(f"DFS inorder tail:  {t2.inorder_tail()}")

    t3 = t2.espejo()
    print(t3)
    print(t3.sin_hojas())


if __name__ == "__main__":
    main()
