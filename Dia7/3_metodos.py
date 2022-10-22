class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):  # siempre lleva "self"
        print("pio")
        print(self.color)  # es la manera de llamar variables dentro de la funcion

    def volar(self, metros):
        print(f"el pajaro ha volado {metros} metros")


mi_pajaro = Pajaro("rojo", "algo")
mi_pajaro.piar()
mi_pajaro.volar(400)
# una vez llenado el contructor se pueden utilizar los metodos de la clase
# ///////////////////////////////////////////////
class Perro:
    def ladrar(self):
        print("Guau!")


class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")


merlin = Mago()
merlin.lanzar_hechizo()


class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")


alarmas = Alarma()
alarmas.postergar(59)
