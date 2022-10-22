"""
La libreria collections ya esta incluida al instalar python
-estructuras de datos
"""
from collections import (
    Counter,
    defaultdict,
    namedtuple,
)  # contador dentro de un diccionario

lista = [1, 1, 1, 1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8, 8, 8]
dic = Counter(lista)  # Muestra el numero de veces que se repite cada numero en la lista
print(type(lista))
print(dic)
print(dic.most_common())  # el numero con mayor numero de repeticiones
print(dic.most_common(1))  # imprime solo el primero, o los primeros 2 o 3 o4
print(f"{list(dic)}\n")  # lo imprimimos como lista y muestra  los valores unicos

print(Counter("misisipisi"))  # Con strings
print(
    Counter(" al pan pan y al vino vino".split())
)  # split sepala el texto por palabras
# /////////////////////////////////////////////////////////////////////////
"""
Default dict libreria
crea un dicionario por defalut
"""
mi_dic = {"uno": "azul", "dos": "amarillo", "tres": "rojo"}
print(mi_dic["uno"])  # imprime el valor de la clave ingresada
print("/" * 30)
default_dic = defaultdict(lambda: "Nada")
default_dic["uno"] = "Animal"
print(default_dic["dos"])
default_dic["cinco"] = "Humanos"
print(default_dic)
# /////////////////////////////////////////////////////////////////////////
"""
namedtuple
"""
print("/" * 30)

mi_tupla = (1, 2, 3, 3)
print(mi_tupla.count(3))  # cantidad de numeros 3 en la tupla
print(mi_tupla[1])  # tupla en posicion 1
print(mi_tupla)

Persona = namedtuple(
    "Persona", ["nombre", "altura", "peso"]
)  # creamos un objeto de una tupla con namedtuple
lala = Persona("Lala", 1.62, 56)  # Creamos un objeto de persona
print(lala.altura, lala.nombre)  # indexamos un valor a una tupla con titulos
print(lala[2])  # Forma tradicional de llamar una posicion en la tupla


# ////////////////////////////////////////////////////////////////////////////////////////////////////
from collections import Counter

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)

from collections import defaultdict

mi_diccionario = defaultdict(lambda: "Valor no hallado")
mi_diccionario["edad"] = 44

# //////////////////DEQUE//////////
"""
sirve para agregar caracteres a una lista o un string al final, o al principio del arreglo
"""
from collections import deque  # libreria

lista_ciudades = deque(
    ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
)  # igualacion a la lista
lista_ciudades.appendleft("CDMX")  # agrega al principio del arreglo
print(lista_ciudades)
