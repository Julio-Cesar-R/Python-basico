class Animales:
    vivo = True

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nace(self):
        print("este animal ha nacido")
        self.vivo = True


class Aves(Animales):
    Alas = True


class Felinos(Animales):
    Garras = True


print(Aves.__bases__)  # para saber de que clase hereda
print(Animales.__subclasses__())  # saber las subclases a las que hereda
pajarito = Aves(1, "verde")
pajarito.vivo = False
print(pajarito.vivo)
pajarito.nace()
print(pajarito.vivo)
print(pajarito.edad)

# ///////////////////////////////////////////////////////////
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Alumno(Persona):
    pass


class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas


class Perro(Mascota):
    pass


class Vehiculo:
    def acelerar(self):
        pass

    def frenar(self):
        pass


class Automovil(Vehiculo):
    pass


# //
