mi_lista=["uno","dos","tres","cuatro"]
mi_lista2=["cinco","seis","siete","ocho"]
print(type(mi_lista))
print(len(mi_lista))
print(mi_lista[0:2])
print(mi_lista[0:])
print(mi_lista + mi_lista2)
mi_lista3= mi_lista + mi_lista2
mi_lista3[0]="1"
mi_lista3.append("nueve")#agregar a la lista en posicion final
mi_lista3.append("diez")
print(mi_lista3)

eliminado=mi_lista3.pop(0)#elimina una posicion en la lista
print(eliminado)# muestra lo que se elimino
print(mi_lista3)# muestra la lista actualizada

lista=["adrian","abi","zorro","hector","octavio"]#ordena la lista en orden alfabetico
lista.sort()
print(lista)
lista.reverse()# ordena al reves
print(lista)
#//////////////////////////////////////////////////////////////

mi_lista=[1,"hola",5.4,"juan","juan2"]

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado=frutas.pop(2)