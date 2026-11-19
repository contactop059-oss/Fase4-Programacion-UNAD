
import logging

from cliente import Cliente, ErrorCliente
from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada,
    ErrorServicio
)
from reserva import Reserva, ErrorReserva


logging.basicConfig(
    filename="sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class SistemaGestion:
    """Sistema de gestión de Software FJ."""

    def __init__(self):
        self.clientes = []
        self.reservas = []

        self.servicios = [
            ReservaSala("S01", "Sala de reuniones", 50000),
            AlquilerEquipo("E01", "Computador portátil", 30000),
            AsesoriaEspecializada(
                "A01", "Asesoría de programación", 80000
            )
        ]

    def registrar_cliente(self):
        try:
            identificacion = input("Identificación: ").strip()
            nombre = input("Nombre completo: ").strip()
            correo = input("Correo electrónico: ").strip()

            if any(
                c.identificacion == identificacion
                for c in self.clientes
            ):
                raise ErrorCliente(
                    "Ya existe un cliente con esa identificación."
                )

            cliente = Cliente(identificacion, nombre, correo)
            self.clientes.append(cliente)

        except ErrorCliente as error:
            logging.exception("Error al registrar cliente")
            print(f"Error: {error}")

        else:
            logging.info(
                "Cliente %s registrado.", identificacion
            )
            print("Cliente registrado correctamente.")

    def consultar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
            return

        for cliente in self.clientes:
            print(cliente.mostrar_informacion())

    def consultar_servicios(self):
        for servicio in self.servicios:
            print(
                f"{servicio.codigo} | "
                f"{servicio.describir()} | "
                f"Tarifa: ${servicio.tarifa:,.2f} | "
                f"Disponible: {servicio.disponible}"
            )

    def buscar_cliente(self, identificacion):
        for cliente in self.clientes:
            if cliente.identificacion == identificacion:
                return cliente

        raise ErrorCliente("Cliente no encontrado.")

    def buscar_servicio(self, codigo):
        for servicio in self.servicios:
            if servicio.codigo == codigo:
                return servicio

        raise ErrorServicio("Servicio no encontrado.")

    def crear_reserva(self):
        try:
            identificacion = input(
                "Identificación del cliente: "
            ).strip()

            cliente = self.buscar_cliente(identificacion)

            self.consultar_servicios()

            codigo_servicio = input(
                "Código del servicio: "
            ).strip()

            servicio = self.buscar_servicio(codigo_servicio)

            if not servicio.disponible:
                raise ErrorReserva(
                    "El servicio seleccionado no está disponible."
                )

            duracion = float(
                input("Duración en horas: ")
            )

            codigo = f"R{len(self.reservas) + 1:03d}"

            reserva = Reserva(
                codigo, cliente, servicio, duracion
            )

            reserva.confirmar()
            self.reservas.append(reserva)

        except (
            ValueError,
            ErrorCliente,
            ErrorServicio,
            ErrorReserva
        ) as error:
            logging.exception("Error al crear reserva")
            print(f"Error: {error}")

        else:
            print("Reserva creada y confirmada correctamente.")

    def consultar_reservas(self):
        if not self.reservas:
            print("No hay reservas registradas.")
            return

        for reserva in self.reservas:
            print(reserva.mostrar_informacion())

    def cancelar_reserva(self):
        try:
            codigo = input(
                "Código de la reserva: "
            ).strip()

            reserva = next(
                (
                    r for r in self.reservas
                    if r.codigo == codigo
                ),
                None
            )

            if reserva is None:
                raise ErrorReserva(
                    "No se encontró la reserva."
                )

            print(reserva.cancelar())

        except ErrorReserva as error:
            logging.exception("Error al cancelar reserva")
            print(f"Error: {error}")

    def procesar_reserva(self):
        try:
            codigo = input(
                "Código de la reserva: "
            ).strip()

            reserva = next(
                (
                    r for r in self.reservas
                    if r.codigo == codigo
                ),
                None
            )

            if reserva is None:
                raise ErrorReserva(
                    "No se encontró la reserva."
                )

            descuento = float(
                input("Descuento (%): ")
            )

            costo = reserva.procesar(descuento)

        except (
            ValueError,
            ErrorReserva
        ) as error:
            logging.exception("Error al procesar reserva")
            print(f"Error: {error}")

        else:
            print(f"Costo total: ${costo:,.2f}")

    def mostrar_menu(self):
        print("\n====================================")
        print(" SOFTWARE FJ - SISTEMA DE GESTIÓN")
        print("====================================")
        print("1. Registrar cliente")
        print("2. Consultar clientes")
        print("3. Consultar servicios")
        print("4. Crear reserva")
        print("5. Consultar reservas")
        print("6. Cancelar reserva")
        print("7. Procesar reserva")
        print("8. Salir")

    def ejecutar(self):
        while True:
            try:
                self.mostrar_menu()
                opcion = input(
                    "Seleccione una opción: "
                ).strip()

                if opcion == "1":
                    self.registrar_cliente()

                elif opcion == "2":
                    self.consultar_clientes()

                elif opcion == "3":
                    self.consultar_servicios()

                elif opcion == "4":
                    self.crear_reserva()

                elif opcion == "5":
                    self.consultar_reservas()

                elif opcion == "6":
                    self.cancelar_reserva()

                elif opcion == "7":
                    self.procesar_reserva()

                elif opcion == "8":
                    print("Gracias por utilizar Software FJ.")
                    break

                else:
                    print("Seleccione una opción válida.")

            except (EOFError, KeyboardInterrupt):
                print("\nPrograma finalizado.")
                break

            except Exception:
                logging.exception(
                    "Error inesperado en el menú principal"
                )
                print(
                    "Ocurrió un error. "
                    "El sistema continuará funcionando."
                )


if __name__ == "__main__":
    sistema = SistemaGestion()
    sistema.ejecutar()
