tdiurna = 10000
tnocturna = 13000
sobrecargo = 0.10

class Turno:
    def __init__(self, horas_trabajadas):
        self.horas_trabajadas = horas_trabajadas

    def calcular_pago(self):
        pass


class TurnoDiurno(Turno):

    def calcular_pago(self):
        if self.horas_trabajadas <= 8:
            pago = self.horas_trabajadas * tdiurna
        else:
            horas_extra = self.horas_trabajadas - 8
            pago = (8 * tdiurna) + (horas_extra * tdiurna * (1 + sobrecargo))

        print("Pago del turno diurno: ", pago)


class TurnoNocturno(Turno):

    def calcular_pago(self):
        if self.horas_trabajadas <= 8:
            pago = self.horas_trabajadas * tnocturna
        else:
            horas_extra = self.horas_trabajadas - 8
            pago = (8 * tnocturna) + (horas_extra * tnocturna * (1 + sobrecargo))

        print("Pago Nocturno: $", pago)

while True:

    print("\n--- MENÚ ---")
    print("1. Turno Diurno")
    print("2. Turno Nocturno")
    print("3. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "3":
        print("Programa finalizado.")
        break

    horas = int(input("Ingrese las horas trabajadas: "))

    if opcion == "1":
        empleado = TurnoDiurno(horas)

    elif opcion == "2":
        empleado = TurnoNocturno(horas)

    else:
        print("Opción inválida.")
        continue

    empleado.calcular_pago()