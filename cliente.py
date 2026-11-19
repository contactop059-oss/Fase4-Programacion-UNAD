
import logging

from entidad import Entidad

logging.basicConfig(
    filename="sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class ErrorCliente(Exception):
    """Excepción personalizada para datos de clientes."""
    pass


class Cliente(Entidad):
    """Representa un cliente de Software FJ."""

    def __init__(self, identificacion, nombre, correo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, valor):
        if not str(valor).strip():
            raise ErrorCliente("La identificación es obligatoria.")
        self.__identificacion = str(valor).strip()

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ErrorCliente("El nombre no puede estar vacío.")
        self.__nombre = valor.strip()

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if (
            not isinstance(valor, str)
            or valor.count("@") != 1
            or "." not in valor.split("@")[-1]
        ):
            raise ErrorCliente("El correo electrónico no es válido.")
        self.__correo = valor.strip()

    def mostrar_informacion(self):
        return (
            f"ID: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )
