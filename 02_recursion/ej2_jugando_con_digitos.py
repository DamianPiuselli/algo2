from typing import Tuple


def cantidad_de_digitos(numero: int) -> int:
    if numero < 10:
        return 1
    else:
        return 1 + cantidad_de_digitos(numero // 10)


def reversa_num(numero: int) -> int:
    if numero < 10:
        return numero
    else:
        return (numero % 10) * 10 ** cantidad_de_digitos(numero // 10) + reversa_num(
            numero // 10
        )


def suma_digitos(numero: int) -> int:
    if numero < 10:
        return numero
    else:
        return numero % 10 + suma_digitos(numero // 10)


def reversa_y_suma(numero: int, acumulado: int = 0) -> Tuple[int, int]:
    if numero == 0:
        return acumulado, 0

    else:
        reversa, suma = reversa_y_suma(numero // 10, acumulado * 10 + numero % 10)
        return reversa, suma + numero % 10


def main():
    numero = 123456
    print(f"La cantidad de digitos de {numero} es {cantidad_de_digitos(numero)}")
    print(f"La reversa de {numero} es {reversa_num(numero)}")
    print(f"La suma de los digitos de {numero} es {suma_digitos(numero)}")

    reversa, suma = reversa_y_suma(numero)
    print(f"La reversa de {numero} es {reversa}")
    print(f"La suma de los digitos de {numero} es {suma}")


if __name__ == "__main__":
    main()
