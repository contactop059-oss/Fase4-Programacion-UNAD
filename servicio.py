
from abc import ABC, abstractmethod
from entidad import Entidad

class ErrorServicio(Exception):
    """Excepción personalizada para servicios."""
    pass


class Servicio(Entidad):
    """Clase abstracta general para los servicios."""

    def __init__(self, codigo, nombre, tarifa):
        if not str(codigo).strip():
            raise ErrorServicio("El código es obligatorio.")

        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorServicio("El nombre es obligatorio.")

        if isinstance(tarifa, bool) or not isinstance(
            tarifa, (int, float)
        ) or not 0 < tarifa < float("inf"):
            raise ErrorServicio("La tarifa debe ser positiva y finita.")

        self.codigo = str(codigo).strip()
        self.nombre = nombre.strip()
        self.tarifa = tarifa
        self.disponible = True

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0):
        """Calcula el costo de un servicio."""
        pass

    @abstractmethod
    def describir(self):
        """Devuelve la descripción del servicio."""
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        """Valida los parámetros del servicio."""
        pass

    def mostrar_informacion(self):
        return (
            f"Código: {self.codigo} | "
            f"Servicio: {self.nombre} | "
            f"Tarifa: ${self.tarifa:,.2f} | "
            f"Disponible: {self.disponible}"
        )

    def verificar_duracion(self, duracion):

    @abstractmethod
    def validar_parametros(self, duracion):
        """Valida los parámetros del servicio."""
        pass

    def verificar_duracion(self, duracion):
        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
            or not 0 < duracion < float("inf")
        ):
            raise ErrorServicio(
                "La duración debe ser un número positivo y finito."
            )

    def aplicar_descuento(self, subtotal, descuento):
        if (
            isinstance(descuento, bool)
            or not isinstance(descuento, (int, float))
            or not 0 <= descuento <= 100
        ):
            raise ErrorServicio(
                "El descuento debe estar entre 0 y 100."
            )

        return subtotal * (1 - descuento / 100)


class ReservaSala(Servicio):
    """Servicio de reserva de salas."""

    def validar_parametros(self, duracion):
        self.verificar_duracion(duracion)

    def calcular_costo(self, duracion, descuento=0):
        self.validar_parametros(duracion)
        subtotal = self.tarifa * duracion
        return self.aplicar_descuento(subtotal, descuento)

    def describir(self):
        return f"Reserva de sala: {self.nombre}"


class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos."""

    def validar_parametros(self, duracion):
        self.verificar_duracion(duracion)

    def calcular_costo(self, duracion, descuento=0):
        self.validar_parametros(duracion)
        subtotal = self.tarifa * duracion
        return self.aplicar_descuento(subtotal, descuento)

    def describir(self):
        return f"Alquiler de equipo: {self.nombre}"


class AsesoriaEspecializada(Servicio):
    """Servicio de asesorías especializadas."""

    def validar_parametros(self, duracion):
        self.verificar_duracion(duracion)

    def calcular_costo(self, duracion, descuento=0):
        self.validar_parametros(duracion)
        subtotal = self.tarifa * duracion
        return self.aplicar_descuento(subtotal, descuento)

    def describir(self):
        return f"Asesoría especializada: {self.nombre}"
