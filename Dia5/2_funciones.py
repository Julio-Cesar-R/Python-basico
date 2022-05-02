#Creacion de funciones
#Las funciones devuelven una variable o en este caso impresiones en consola
#funciones
import re

def funcion():
    print("Hola munndo")
funcion()

def sumar(num1,num2):
    """
    Esta funcion suma dos numeros enteros
    Ejemplo:
    sumar(23,45)
    """
    if type(num1)== type(num2)==type(10):
        res=0
        res=num1+num2
        return res
    else:
        return f"Uno de los valores que estas ingresando no es correcto\nnum1 {type(num1)} num2 {type(num2)}"

#///
sum_res=sumar("hi",56)
print(f"El resultado de la suma es {sum_res}")
def mi_funcion(nombre):
    '''
    este codigo  recibe un string
    mediante el cual regresa una cadena de caracteres
    '''
    print(f" hola {nombre}")

mi_funcion(" Carlos") #llamada al metodo"mi_funcion"

#Funciones que no reciben parametros
def saludar():

    print("¡Hola mundo!")

#Funcion con cadena de caracteres
def bienvenida(nombre):
    print(f"¡Bienvenido {nombre}")


nombre_persona = "Kaiser"
bienvenida(nombre_persona)

#Funcion que recibe un numero
def cuadrado(un_numero):
    print(un_numero ** 2)
un_numero = 5


# Ambito de variables
# Ver la diferencia entre variables locales y de funcion
from numpy import var #libreria

var=5#Variable global

def funcion():
    var=8 #Variable interna de la funcion
    print(var)

print(var)
funcion()