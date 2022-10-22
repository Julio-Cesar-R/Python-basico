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

    def pintar_negro(self):  # metodo de instancia modifica variables y llama metodos
        self.color = "negro"

    @classmethod
    def poner_huevo(cls, cantidad):  # clase de metodo
        print(f"la cantidad de huevos fue {cantidad}")
        cls.alas = True  # Puede modificar las variables de una clase

    @staticmethod
    def mirar():  # clase estatica, no cambia atributos
        print("el pajaro mira")
        pass


mi_pajaro = Pajaro("rojo", "algo")
mi_pajaro.piar()
mi_pajaro.volar(400)
mi_pajaro.pintar_negro()
print(mi_pajaro.color)
mi_pajaro.alas = False  # se puede modificar la clase
print(mi_pajaro.alas)
print("\n///////////////CLASS METHOD///////////////")
mi_pajaro.poner_huevo(44)
Pajaro.poner_huevo(55)  # no es necesario crear una instancia
print("\n///////////////CLASS STATIC///////////////")
Pajaro.mirar()  # llamada al metodo estatico

# ///////////////////////////////////////////////////////////////////////////////
class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True


class Saludo:
    @staticmethod
    def decir():
        print("Hola")


class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas - 1
