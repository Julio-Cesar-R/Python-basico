#/// IMPORTANTE
# Poo


class Persona():
    texto = ""

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        self.texto = f"Hola mi nombre es {self.nombre}"
        return self.texto


objeto = Persona("Julio", "Rosas")
print(objeto.nombre)
print(objeto.apellido)
print(type(objeto))
re = objeto.saludar()
print(re)


class Adulto(Persona):
    def __init__(self, nombre, apellido):
        Persona.__init__(self, nombre, apellido)

    def saludar(self):
        self.texto = "Hola soy adulto"
        return self.texto

    def grabar_tarjeta(self, tarjeta):
        self.tarjeta = tarjeta

    def __str__(self):
        self.texto = f"Nombre:{self.nombre} Apellido:{self.apellido} Tajeta: {self.tarjeta}"
        return self.texto


ob = Adulto("Kai", "Fox")
print(type(ob))
texto1 = ob.saludar()
print(texto1)

ob.grabar_tarjeta("nkhjkfhsdfufhwflaks")

# Funcion especial STR def __str__(self) :

print(ob)
#///////////////////////////////////
class Animales:
    vivo=True
    def __init__(self,edad,color):
        self.edad=edad
        self.color=color

    def nace(self):
        print("este animal ha nacido")
        self.vivo=True
    def habla(self):
        print("hablo")

class Aves(Animales):
    Alas=True
    def __init__(self,edad,color,altura):#puede tener su propio constructor siguiendo la estructura del init del que hereda
        super().__init__(edad,color)# son los selfs de la clase padre(Asignaciones heredadas)
        self.altura=altura#solo se especifica este nuevo atributo
    def habla(self):
        print("pio")
    def volar(self,metros):
        print(f"el pajaro volo {metros} metros")



pajarito=Aves(1,"Rojo",50)
pajarito.habla()#aunque existan dos metodos en este caso imprimira el propio
pajarito.volar(599)
print(pajarito.altura)

class Padre:
    def hablar(self):
        print("Hablar hola")
class Madre:
    def reir(self):
        print("jajajjajajaj")
    def hablar(self):
        print(" hola hola cara de bola")
class Hijo(Madre,Padre):
    pass
class Nieto(Hijo):
    pass
print(f"HERENCIA MULTIPLE")
mi_nieto=Nieto()
mi_nieto.hablar()
mi_nieto.reir()
print(Nieto.__mro__)#el oden de prioridad de ejecucion de metodos
#////////////////////////////////////////////////////////////
class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")

class Hija(Madre, Padre):
    pass
#/////////////////////////////////////
class Vertebrado():
    vertebrado = True


class Ave(Vertebrado):
    tiene_pico = True

    def poner_huevos(self):
        print("Poniendo huevos")


class Reptil(Vertebrado):
    venenoso = True


class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")

    def poner_huevos(self):
        print("Poniendo huevos")


class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")

    def amamantar(self):
        print("Amamantando crías")


class Ornitorrinco(Mamifero, Pez, Reptil, Ave):
    pass
#/////////////////////////////////////////////////
class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"


class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"
kaiser=Hijo()
print(kaiser.hobby())





