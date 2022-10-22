class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice Muuu")


class Obeja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice Beeee")


vaca1 = Vaca("Aurora")
obeja1 = Obeja("Nube")
vaca1.hablar()
obeja1.hablar()

animales = [vaca1, obeja1]
for animal in animales:
    animal.hablar()  # ejecuta la misma funcion en dos metodos distintos con diferentes instancias"


def animal_habla(animal):  # en una funcion que llama a la clase
    animal.hablar()


animal_habla(vaca1)
animal_habla(obeja1)
# ///////////////////////////////////////////////////
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for dato in [palabra, lista, tupla]:
    print(len(dato))


class Mago:
    def atacar(self):
        print("Ataque mágico")


class Arquero:
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai:
    def atacar(self):
        print("Ataque con katana")


samurai = Samurai()
arquero = Arquero()
mago = Mago()
personajes = [arquero, mago, samurai]
for lista in personajes:
    lista.atacar()
# /////////////////////////////////////////
class Mago:
    def defender(self):
        print("Escudo mágico")


class Arquero:
    def defender(self):
        print("Esconderse")


class Samurai:
    def defender(self):
        print("Bloqueo")


samurai = Samurai()
arquero = Arquero()
mago = Mago()
personajes = [arquero, mago, samurai]


def personaje_defender(lista_personajes):
    for lista in lista_personajes:
        lista.defender()


personaje_defender(personajes)


def personaje_defende(personaje):
    personaje.defender()


personaje_defende(mago)
