
from abc import ABC, abstractmethod


class Entidad(ABC):
    """Clase abstracta general del sistema Software FJ."""

    @abstractmethod
    def mostrar_informacion(self):
        """Devuelve la información de una entidad."""
        pass
