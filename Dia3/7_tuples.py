# Tuplas en py
tuplas = (1, 2, 5, "Hola")
print(type(tuplas))
print(tuplas)
# La tupla es inmutable
elemento = tuplas[0]
print(elemento)
print(tuplas[1:3])

# No se pueden modificar

mi_tuple = (1, 2, (23, 45), 4)
print(mi_tuple[3])
print(mi_tuple[2][1])
mi_tuple = list(mi_tuple)
mi_tuple.append(55)
print(mi_tuple)
mi_tuple = tuple(mi_tuple)
print(mi_tuple)
print(type(mi_tuple))

t = (1, 2, 3, 1)  # asigna el valor de la tupla a las variables
a, b, c, d = t
print(a, b, c)
print(len(t))
print(t.count(1))  # numero de unos que aparecen en la tupla
print(t.index(3))  # busca la posicion en la que se encuentra la informacion
# //////////////////////////////////////////////////////////////////////
mi_tuplaa = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tuplaa.count(2))

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)
print(type(mi_lista))

mi_tupla1 = (1, 2, 3, 4)
a, b, c, d = mi_tupla1
