texto = input("ingrese un texto: ").lower()
letras = []
letras.append(input("ingresa una letra: "))
letras.append(input("ingresa otra letra: "))
letras.append(input("ingresa y otra letra "))
print(letras)
print(
    f" el resultado de la letra {letras[0]} dentro del texto es: {letras[0] in texto}"
)
print(
    f" el resultado de la letra {letras[1]} dentro del texto es: {letras[1] in texto}"
)
print(
    f" el resultado de la letra {letras[2]} dentro del texto es: {letras[2] in texto}"
)
le1 = texto.count(letras[0])
le2 = texto.count(letras[1])
le3 = texto.count(letras[2])
print(f"la letra {letras[0]} se repite {le1} veces")
print(f"la letra {letras[1]} se repite {le2} veces")
print(f"la letra {letras[2]} se repite {le3} veces")

palabra = texto.split()
palabras = len(palabra)
print(f"la cantidad de palabras son {palabras}")
print(f"la primera letra es {texto[0]}")
print(f"la ultima letra es {texto[-1]}")

palabra.reverse()
texto_invertido = " ".join(palabra)
print(f"Si ordenamos tu texto al revés va a decir: '{texto_invertido}'")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = "python" in texto
dic = {True: "sí", False: "no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")
