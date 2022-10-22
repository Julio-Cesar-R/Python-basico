# buscar una posicion en una cadena o un caracter especifico

texto = "Los indices se utilizan para determinar la posicion de un caracter dentro de una cadena de texto"
posicion = texto[2]
print(posicion)
print(texto[-3])

posicion1 = texto.index(
    "la", 0, 50
)  # busca un caracter o una palabra en particular en la cadena de texto, el primero que aparece
print(posicion1)
posicion2 = texto.rindex("e")
print(posicion2)

palabra = "ordenador"
print(palabra[4])

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index("práctica"))

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.rindex("práctica"))
