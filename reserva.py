
import logging
from cliente import Cliente
from servicio import Servicio, ErrorServicio

logging.basicConfig(
    filename="sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class ErrorReserva(Exception):
    """Excepción personalizada para las reservas."""
    pass


class Reserva:
    """Gestiona las reservas de Software FJ."""

    def __init__(self, codigo, cliente, servicio, duracion):
        if not str(codigo).strip():
            raise ErrorReserva(
                "El código de reserva es obligatorio."
            )

        if not isinstance(cliente, Cliente):
            raise ErrorReserva("El cliente no es válido.")

        if not isinstance(servicio, Servicio):
            raise ErrorReserva("El servicio no es válido.")

        try:
            servicio.validar_parametros(duracion)
        except ErrorServicio as error:
            raise ErrorReserva(
                "La duración de la reserva no es válida."
            ) from error

        self.codigo = str(codigo).strip()
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

        logging.info(
            "Reserva %s creada correctamente.", self.codigo
        )

    def confirmar(self):
        try:
            if self.estado != "Pendiente":
                raise ErrorReserva(
                    "Solo se pueden confirmar reservas pendientes."
                )

            if not self.servicio.disponible:
                raise ErrorReserva(
                    "El servicio no está disponible."
                )

        except ErrorReserva:
            logging.exception(
                "Error al confirmar la reserva %s", self.codigo
            )
            raise

        else:
            self.estado = "Confirmada"
            logging.info(
                "Reserva %s confirmada.", self.codigo
            )
            return "Reserva confirmada correctamente."

        finally:
            logging.info(
                "Finalizó el intento de confirmación %s.",
                self.codigo
            )

    def cancelar(self):
        try:
            if self.estado == "Cancelada":
                raise ErrorReserva(
                    "La reserva ya está cancelada."
                )

            if self.estado == "Procesada":
                raise ErrorReserva(
                    "No se puede cancelar una reserva procesada."
                )

            self.estado = "Cancelada"
            logging.info(
                "Reserva %s cancelada.", self.codigo
            )
            return "Reserva cancelada correctamente."

        except ErrorReserva:
            logging.exception(
                "Error al cancelar la reserva %s", self.codigo
            )
            raise

    def procesar(self, descuento=0):
        try:
            if self.estado != "Confirmada":
                raise ErrorReserva(
                    "La reserva debe estar confirmada."
                )

            if not self.servicio.disponible:
                raise ErrorReserva(
                    "El servicio no está disponible."
                )

            costo = self.servicio.calcular_costo(
                self.duracion, descuento
            )

        except ErrorServicio as error:
            logging.exception(
                "Error de servicio en reserva %s", self.codigo
            )
            raise ErrorReserva(
                "No fue posible calcular el costo."
            ) from error

        except ErrorReserva:
            logging.exception(
                "Error al procesar reserva %s", self.codigo
            )
            raise

        else:
            self.estado = "Procesada"
            logging.info(
                "Reserva %s procesada. Costo: %.2f",
                self.codigo, costo
            )
            return costo

        finally:
            logging.info(
                "Finalizó el procesamiento de %s.",
                self.codigo
            )

    def mostrar_informacion(self):
        return (
            f"Reserva: {self.codigo} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Duración: {self.duracion} | "
            f"Estado: {self.estado}"
        )
