"""
este programa lo usaremos para generar algo sin tener que usar
mucha memoria guardandolo en una lista

def generador():

    for n in range(1,5):
        yield n*10
g=generador()#Creamos un objeto de esta funcion
print(next(g))#Invocamos el metodo para que se imprima en pantalla

"""
"""
def mi_generador():
    x=1
    yield x
    x+=1
    yield x
    x += 1
    yield x
    x += 1
gen=mi_generador()
print(next(gen))
print(next(gen))
print(next(gen))
"""
"""
def mi_generador():
    x=1
    while x>=1:
        yield x
        x+=1

generador=mi_generador()
print(next(generador))
print(next(generador))
print(next(generador))"""


def mi_generador():
    x = 1
    while True:
        res = 7 * x
        yield res
        x += 1


generador = mi_generador()
print(next(generador))
print(next(generador))
print(next(generador))


def vidas():
    x = "Te quedan 3 vidas"
    yield x

    x = "Te quedan 2 vidas"
    yield x

    x = "Te queda 1 vida"
    yield x

    x = "Game Over"
    yield x


perder_vidas = vidas()
print(next(perder_vidas))
