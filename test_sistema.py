
import unittest

from entidad import Entidad
from cliente import Cliente, ErrorCliente
from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada,
    ErrorServicio
)
from reserva import Reserva, ErrorReserva


class TestSistemaSoftwareFJ(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente(
            "123456789", "Juan Perez", "juan.perez@gmail.com"
        )
        self.sala = ReservaSala("S01", "Sala de reuniones", 50000)

    def test_01_registro_cliente(self):
        self.assertEqual(self.cliente.nombre, "Juan Perez")

    def test_02_herencia_cliente(self):
        self.assertIsInstance(self.cliente, Entidad)

    def test_03_correo_invalido(self):
        with self.assertRaises(ErrorCliente):
            Cliente("987654321", "Maria Lopez", "maria.com")

    def test_04_creacion_servicio(self):
        self.assertEqual(self.sala.tarifa, 50000)

    def test_05_tarifa_invalida(self):
        with self.assertRaises(ErrorServicio):
            ReservaSala("S02", "Sala", -50000)

    def test_06_calculo_sala(self):
        self.assertEqual(self.sala.calcular_costo(2, 10), 90000)

    def test_07_calculo_equipo(self):
        equipo = AlquilerEquipo("E01", "Portátil", 30000)
        self.assertEqual(equipo.calcular_costo(2, 10), 54000)

    def test_08_calculo_asesoria(self):
        asesoria = AsesoriaEspecializada(
            "A01", "Asesoría", 80000
        )
        self.assertEqual(
            asesoria.calcular_costo(2, 10), 144000
        )

    def test_09_reserva_confirmada(self):
        reserva = Reserva("R001", self.cliente, self.sala, 2)
        reserva.confirmar()
        self.assertEqual(reserva.estado, "Confirmada")

    def test_10_reserva_procesada(self):
        reserva = Reserva("R002", self.cliente, self.sala, 2)
        reserva.confirmar()
        self.assertEqual(reserva.procesar(10), 90000)
        self.assertEqual(reserva.estado, "Procesada")

    def test_11_cancelacion_invalida(self):
        reserva = Reserva("R003", self.cliente, self.sala, 2)
        reserva.confirmar()
        reserva.procesar()
        with self.assertRaises(ErrorReserva):
            reserva.cancelar()

    def test_12_duracion_invalida(self):
        with self.assertRaises(ErrorReserva):
            Reserva("R004", self.cliente, self.sala, -2)


if __name__ == "__main__":
    unittest.main()
