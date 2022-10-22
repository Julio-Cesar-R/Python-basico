from random import *

aleatorio = randint(1, 101)
print(aleatorio)
acerto = False
contador = 0
nombre = input(" ingresa tu nombre: ")
print(f"{nombre} he elegido un numero al azar del 1 al 1000, trata de adivinar cual es")
while acerto == False:
    contador += 1
    respuesta = int(input("ingresa el numero que crees que sea: "))
    if respuesta not in range(1, 101):
        print(" esta fuera del rango")
    elif respuesta > aleatorio:
        print(" tu numero esta por encima del  numero elegido")

    elif respuesta < aleatorio:
        print(" tu numero esta por debajo del  numero elegido")

    else:
        print("tu numero coincide felicidades")
        acerto = True
        print(f"el numero de intentos que tardaste en adivinar fueron {contador}")
