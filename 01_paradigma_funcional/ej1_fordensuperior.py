from typing import Callable, Any


def wrapper(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    print(f"Ejecutando {func.__name__}()")
    return func(*args, **kwargs)


def suma(a: int, b: int) -> int:
    return a + b


def saludo(nombre: str, mensaje: str = "Hola") -> str:
    return f"{mensaje}, {nombre}!"


if __name__ == "__main__":
    resultado_suma: int = wrapper(suma, 5, 3)
    print(f"Resultado de suma: {resultado_suma}")

    resultado_saludo: str = wrapper(saludo, "Juan", mensaje="Buenos días")
    print(f"Resultado de saludo: {resultado_saludo}")
