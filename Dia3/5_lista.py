# Listas
lista = [1, 2, 3, "Juan", [1, 9, 8, 7]]
print(type(lista))
print(lista)
print(lista[-1][0])

print(lista[1:3])
lista2 = ["Kai", "Fox"]
lista.append(lista2)  # Agrega una lista dentro de una lista
print(lista)
lista3 = ["Xof", "Kaii"]
lista.extend(lista3)  # extend sirve para agregar una lista solo como elementos
print(lista)

lista = [1, 2, 3, "Kaiser"]
print(lista)
# Eliminar un elemto de lista
lista.pop()
print(lista)
lista.pop(0)
print(lista)

# Invertir la lista
lista2 = [1, 2, 3, "Kaiser"]
lista2.reverse()
print(lista2)
# Ordenar una lista
lista3 = [3, 44, 2, 87, 999, 0]
lista3.sort()
print(lista3)
lista4 = ["a", "t", "b"]
lista4.sort()
print(lista4)

lista5 = [1, 2, 3, 4, ["verde", "rojo"]]
print(lista5[4][1])

# Lista de compresion
lista6 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
listanueva = [elemento[0] for elemento in lista6]
print(listanueva)


mi_lista = ["uno", "dos", "tres", "cuatro"]
mi_lista2 = ["cinco", "seis", "siete", "ocho"]
print(type(mi_lista))
print(len(mi_lista))
print(mi_lista[0:2])
print(mi_lista[0:])
print(mi_lista + mi_lista2)
mi_lista3 = mi_lista + mi_lista2
mi_lista3[0] = "1"
mi_lista3.append("nueve")  # agregar a la lista en posicion final
mi_lista3.append("diez")
print(mi_lista3)

eliminado = mi_lista3.pop(0)  # elimina una posicion en la lista
print(eliminado)  # muestra lo que se elimino
print(mi_lista3)  # muestra la lista actualizada

lista = [
    "adrian",
    "abi",
    "zorro",
    "hector",
    "octavio",
]  # ordena la lista en orden alfabetico
lista.sort()
print(lista)
lista.reverse()  # ordena al reves
print(lista)
# //////////////////////////////////////////////////////////////

mi_lista = [1, "hola", 5.4, "juan", "juan2"]

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
