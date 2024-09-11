from typing import Callable


def contador_de_letras(letra: str) -> Callable[[str], int]:
    def contar_letras(string: str) -> int:
        return string.count(letra)

    return contar_letras


if __name__ == "__main__":
    list_de_cadenas = ["hola", "mundo", "python", "es", "genial", "aaAa"]

    contador = contador_de_letras("a")

    print(*map(contador, list_de_cadenas))
