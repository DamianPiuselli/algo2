from abc import ABC, abstractmethod
from typing import List, Optional


# Clase abstracta Zona
class Zona(ABC):
    def __init__(self):
        self.subzonas: List["Zona"] = []

    def agregar_subzona(self, subzona: "Zona") -> None:
        """Agrega una subzona a la lista de subzonas."""
        self.subzonas.append(subzona)

    @abstractmethod
    def censar(self) -> int:
        """Método abstracto que debe ser implementado por todas las subclases."""
        pass


# Clase Vivienda (no tiene subzonas, solo habitantes)
class Vivienda(Zona):
    def __init__(self, habitantes: int):
        super().__init__()
        self.habitantes = habitantes

    def censar(self) -> int:
        """Devuelve el número de habitantes de la vivienda."""
        return self.habitantes


# Clase genérica para cualquier zona que tiene subzonas (País, Provincia, Ciudad, etc.)
class ZonaConSubzonas(Zona):
    def __init__(self, nombre: str):
        super().__init__()
        self.nombre = nombre

    def censar(self) -> int:
        """Censa recursivamente todas las subzonas y suma sus habitantes."""
        total_habitantes = 0
        for subzona in self.subzonas:
            total_habitantes += subzona.censar()  # Llamada recursiva
        return total_habitantes


# Ejemplo de uso:
# Crear una estructura de zonas
pais = ZonaConSubzonas("Argentina")
provincia1 = ZonaConSubzonas("Buenos Aires")
provincia2 = ZonaConSubzonas("Córdoba")
ciudad1 = ZonaConSubzonas("Ciudad de Buenos Aires")
ciudad2 = ZonaConSubzonas("La Plata")
ciudad3 = ZonaConSubzonas("Córdoba")

# Agregar viviendas a las ciudades
ciudad1.agregar_subzona(Vivienda(500))
ciudad1.agregar_subzona(Vivienda(300))
ciudad2.agregar_subzona(Vivienda(200))
ciudad3.agregar_subzona(Vivienda(400))

# Agregar ciudades a las provincias
provincia1.agregar_subzona(ciudad1)
provincia1.agregar_subzona(ciudad2)
provincia2.agregar_subzona(ciudad3)

# Agregar provincias al país
pais.agregar_subzona(provincia1)
pais.agregar_subzona(provincia2)

# Censar el país
habitantes_totales = pais.censar()
print(f"Total de habitantes en el país: {habitantes_totales}")
