from random import *

"""
palitos=["-","--","---","----"]

def mezclar(lista):
    shuffle(lista)
    return lista

def intento():
    intento=""
    while intento not in ["1","2","3","4"]:
        intento=input(" ingresa un numero del 1 al 4: ")
    return int(intento)

def chequeo (lista,intento):
    if lista[intento-1]=="-":
        print("te toco el palito mas corto a lavar los trastes")
    else:
        print("te salvaste")
    print(f"te ha tocado el palito {lista[intento-1]}")



lista= mezclar(palitos)
intento= intento()
resultado= chequeo(lista,intento)
print(resultado)
print(lista)
"""
# ////////////////////////////////////////////////////////////////


def lanzar_dados():
    random1 = randint(1, 6)
    random2 = randint(1, 6)
    return random1, random2


def evaluar_jugada(n1, n2):
    suma_dados = int(n1 + n2)
    if suma_dados <= 6:
        return f"la suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"la suma de tus dados es {suma_dados}. Tienes buenas chances"

    else:
        return f"la suma de tus dados es {suma_dados}. Parece una jugada ganadora"


res1, res2 = lanzar_dados()
res3 = evaluar_jugada(res1, res2)


lista_numeros = [1, 2, 15, 7, 2, 8]


def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista


def promedio(lista):
    valor_medio = sum(lista) / len(lista)
    return valor_medio


lista_numeros = [1, 2, 15, 7, 2, 8]

import random


def lanzar_moneda():
    resultado = ""
    resultado = random.choice(["Cara", "Cruz"])
    return resultado


def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif moneda == "Cruz":
        print("La lista fue salvada")
        return lista


lanzamiento1 = lanzar_moneda()
res = probar_suerte(lanzamiento1, lista_numeros)
print(res)
