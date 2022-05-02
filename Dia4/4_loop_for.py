#Ciclo for

lista=[1,2,3,4]

nueva_lista=[]

for elemento in lista:
    print(elemento)
    nueva_lista.append(elemento)
print(nueva_lista)

#Rango
numeros=range(1,100,10)
print(numeros)
for n in numeros:
    print(n)

for elemnto in range(5):
    print("Hola")


#Acceder a un diccionario
diccionario={"clave1":"valor2", "clave2":"valor2"}

for n in diccionario:
    print(n)
    print(diccionario[n])

#Acceder a una tupla
lista=[(1,2),(3,4)]
print(lista)
for n, n2 in lista:
    print(n)
    print(n2)
#////
#Ejemp1
lista=["a","b","c","d"]
for ciclos in lista:
    numero= lista.index(ciclos)+1#Posicion de la lista
    print(f"posicion {numero} letra {ciclos}")


#Ejemp2
lista=["ana","julio","hector","juan"]
for nombre in lista:
    if(nombre.startswith("j")):
        print(f"el nombre {nombre} comienza con J")
    else:
        print(f"el nombre {nombre} no comienza con J")


#Ejemp 3
numeros=[1,2,3,4,5]
valor=0
for numero in numeros:
    valor=valor+numero
    print(f"El valor en la vuelta {numeros.index(numero)+1} es igual a {valor}")


print(f"el valor al final es de {valor}")

# Ejemp 4
for letra in "python":
    print(letra)

# Ejemp 5
for objeto in[[1,2],[3,4],[5,6]] :#listas
    print(objeto)
# Ejemp 6
for a,b in[[1,2],[3,4],[5,6]] :#se asigna el valor al numero de variables declaradas en el ciclo
    print(a)
    print(b)
# Ejemp 6
dic={"c1":"hola","c2":"adios"}
for clave in dic.items():
    print(clave)

 #///////////////////////////////////////////////////////////////////////////
#Ejercicios
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for nombre in alumnos_clase:
    print(f"Hola {nombre}")

lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_numeros = 0
for numero in lista_numeros:
    suma_numeros = suma_numeros + numero

lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_pares = 0
suma_impares = 0
for numero in lista_numeros:
    if (numero % 2== 0):
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero
