class Pajaro:
    alas = True  # variables globales e iguales para todas las futuras instancias a esta clase

    def __init__(self, color, nombre, edad):  # define la variable en un constructor
        self.color = color
        self.nombre = nombre
        self.edad = edad


mi_pajaro = Pajaro("rojo", "Pedro", 17)  # LLenar el constructor
print(
    f"El nombre del pajaro es {mi_pajaro.nombre} tiene una edad de {mi_pajaro.edad} años y es de color {mi_pajaro.color}"
)
print(Pajaro.alas)  # mostrar variables globales
print(mi_pajaro.alas)  # el objeto creado tambien posee las variables globales
# ///////////////////////////////////////////////////////////////////////////
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


casa_blanca = Casa("blanco", 4)


class Cubo:
    caras = 6

    def __init__(self, color):
        self.color = color


cubo_rojo = Cubo("rojo")


class Personaje:
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad


harry_potter = Personaje("Humano", True, 17)
