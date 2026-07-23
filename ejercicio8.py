class MetodoPago:
    def procesar_pago(self, monto):
        pass


class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto):
        if monto > 0:
            print(f"Pago en efectivo realizado por ${monto}")
        else:
            print("Monto no válido")


class PagoTransferencia(MetodoPago):
    def procesar_pago(self, monto):
        if monto > 0:
            print(f"Transferencia realizada por ${monto}")
        else:
            print("Monto no válido")


class PagoTarjeta(MetodoPago):
    def procesar_pago(self, monto):
        if monto > 0:
            print(f"Pago con tarjeta realizado por ${monto}")
        else:
            print("Monto no válido")


metodos = []

while True:
    print("\n====== MENÚ ======")
    print("1. Agregar pago en efectivo")
    print("2. Agregar pago por transferencia")
    print("3. Agregar pago con tarjeta")
    print("4. Procesar todos los pagos")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        monto = float(input("Ingrese el monto: "))
        metodos.append((PagoEfectivo(), monto))

    elif opcion == 2:
        monto = float(input("Ingrese el monto: "))
        metodos.append((PagoTransferencia(), monto))

    elif opcion == 3:
        monto = float(input("Ingrese el monto: "))
        metodos.append((PagoTarjeta(), monto))

    elif opcion == 4:
        if len(metodos) == 0:
            print("No hay pagos registrados.")
        else:
            print("\nProcesando pagos...\n")
            for metodo, monto in metodos:
                metodo.procesar_pago(monto)

    elif opcion == 5:
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")