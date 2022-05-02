from random import *
al=round (uniform(1,100) ,1)#numero con punto
print(al)

lista=["azul"," verde","rojo"]#elige de manera aleatoria  algo en la lista
aleatorio= choice(lista)
print(aleatorio)

lista1=list(range(3,100,2))
shuffle(lista1)
print(lista1)

#//////////////////////////////////////////////////////
from random import randint
aleatorio= randint(1,11)
print(aleatorio)

from random import *
aleatorio= random()
print(aleatorio)

from random import *
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo= choice(nombres)
