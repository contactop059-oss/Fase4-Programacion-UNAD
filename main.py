
def mostrar_menu():
    print("\n====================================")
    print(" SOFTWARE FJ - SISTEMA DE GESTIÓN")
    print("====================================")
    print("1. Registrar cliente")
    print("2. Consultar clientes")
    print("3. Consultar servicios")
    print("4. Crear reserva")
    print("5. Consultar reservas")
    print("6. Cancelar reserva")
    print("7. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "7":
            print("Gracias por utilizar Software FJ.")
            break
        elif opcion in ("1", "2", "3", "4", "5", "6"):
            print("Esta función se implementará próximamente.")
        else:
            print("Error: seleccione una opción válida.")


if __name__ == "__main__":
    main()
