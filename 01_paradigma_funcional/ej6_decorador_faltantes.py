from typing import TypeVar, Any, Callable, Optional
from functools import wraps

T = TypeVar("T")
R = TypeVar("R")

# Uso optional porque puedo devolver None, dependiendo del input de la funcion original.


def acepta_no_valor(func: Callable[[T], R]) -> Callable[[Optional[T]], Optional[R]]:
    @wraps(func)
    def wrapper(arg: Optional[T]) -> Optional[R]:
        if arg is None:
            return None
        return func(arg)

    return wrapper


@acepta_no_valor
def square(param: float) -> float:
    return param**2


if __name__ == "__main__":
    print(square(4))
    print(square(None))
