class SolicitudCredito:
    def __init__(self, edad, antiguedad=None, ingresos=None):
        self.edad = edad
        self.antiguedad = antiguedad
        self.ingresos = ingresos

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def cumple_perfil_estandar(self):
        return self.antiguedad >= 3 and self.ingresos > 2500

    def cumple_perfil_gold(self):
        return self.ingresos >= 4000

    def evaluar_credito(self):
        if not self.es_mayor_de_edad():
            return False

        perfiles = [
            self.cumple_perfil_estandar(),
            self.cumple_perfil_gold(),
        ]
        return any(perfiles)


def solicitar_datos():
    edad = int(input("Edad: "))
    antiguedad = None
    ingresos = None
    if edad >= 18:
        antiguedad = int(input("Antigüedad en el sistema financiero: "))
        ingresos = int(input("Ingreso mensual: "))
    return edad, antiguedad, ingresos


def main():
    edad, antiguedad, ingresos = solicitar_datos()
    solicitud = SolicitudCredito(edad, antiguedad, ingresos)

    if solicitud.evaluar_credito():
        print("Se aprueba el crédito")
    else:
        print("No se aprueba el crédito")


main()
