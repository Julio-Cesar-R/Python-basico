texto = "Este es un texto de prueba, manipulacion de datos"
resultado = texto.upper()  # texto en mayusculas

print(resultado)
resultado = resultado.lower()  # texto en minusculas
print(resultado)

resultado = resultado.split("e")  # mete la cadena segmentada en una lista
print(resultado)

A = "El"
B = "Merol"
C = "es"
D = "cultura"
E = " ".join([A, B, C, D])  # une una cadena de caracteres de una lista
print(type(E))
print(E)

res = texto.find("a")  # encuentra la posicion dentro de la cadena

print(f"se encuentra en la posicion : {res}")

re = texto.replace("a", "x")  # cambia el texto de una cadena reemplazando
print(re)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////

frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())

lista_palabras = ["La", "legibilidad", "cuenta."]
a = " ".join(lista_palabras)
print(a)

a = "Si la implementación es difícil de explicar, puede que sea una mala idea."

b = a.replace("difícil", "fácil")
c = b.replace("mala", "buena")
print(c)
