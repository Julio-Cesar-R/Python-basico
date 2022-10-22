# Sets
# Conjuntos con py
# No se pueden repetir valores
from numpy import conj

conjunto = set()
print(type(conjunto))

for n in range(1, 33, 2):

    conjunto.add(n)

conjunto.add("kaiser")
print(conjunto)  # Muestra el conjunto ordenado

conjunto.discard("kaiser")
conjunto.discard(1)
print(conjunto)

# Eliminar valores repetidos de una lista
lista = [1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
conju = set(lista)
print(conju)
# ////
# Ejemplos
mi_set = set((1, 2, 3, 4))
s2 = set((11, 22, 33))
print(type(mi_set))
print(mi_set)

print(2 in mi_set)  # "busqyeda true or false"
print(len(mi_set))  # Tamaño del set
s3 = mi_set.union(s2)  # une dos sets
print(s3)

misett = set((1, 2, 3))
misett.add(4)  # agregar al set
print(misett)
misett.remove(1)  # remover del set
print(misett)
misett.discard(3)  # descarta mas no elimina
print(misett)
misett.pop()  # elimina aleatoriamente si no se especifica
print(misett)
misett.clear()  # limpia el set
print(misett)


# ///////////////////////////////////////////////////////////////////////////
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")
