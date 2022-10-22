lista = ["a", "b", "c"]  # enumera los caracteres de la lista
for indice, letra in enumerate(lista):
    print(indice, letra)
lista = ["a", "b", "c"]
tuple = list(enumerate(lista))
print(tuple)
# ///////////////////////////////////////////////////////////
lista_nombres = [
    "Marcos",
    "Laura",
    "Mónica",
    "Javier",
    "Celina",
    "Marta",
    "Darío",
    "Emiliano",
    "Melisa",
]
indice = 0
for nombre in lista_nombres:
    print(f"{nombre} se encuentra en el índice {indice}")
    indice += 1

lista_indices = list(enumerate("Python"))

lista_nombres = [
    "Marcos",
    "Laura",
    "Mónica",
    "Javier",
    "Celina",
    "Marta",
    "Darío",
    "Emiliano",
    "Melisa",
]

for i, nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(i)


lista_nombres = [
    "Marcos",
    "Laura",
    "Mónica",
    "Javier",
    "Celina",
    "Marta",
    "Darío",
    "Emiliano",
    "Melisa",
]

for i, nom in enumerate(lista_nombres):
    if nom.startswith("M"):
        print(i)
