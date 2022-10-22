# Ciclo while

# Cicllo while anidado
valor = True
n = 0
while valor == True:

    while n <= 10:
        print(n)
        n += 1
    valor = False


monedas = 10
while monedas > 0:
    print(f"tengo {monedas} monedas")
    monedas = monedas - 1  # El incremento es necesario para determinar el fin del ciclo
else:
    print("no hay mas mendas")

respuest = "s"
while respuest == "s":
    respuest = input("quieres continuar (s/n)")
else:
    print("gracias")

# Detener un ciclo mediante la innnstruccion break
nombre = input("ingresa tu nombre: ")
for letras in nombre:
    if letras == "u":
        break  # detiene el ciclo
    print(letras)

# Pausar el cilo por una iteracion y continuar con el ciclo
nombre = input("ingresa tu nombre: ")
for letras in nombre:
    if letras == "u":
        continue  # se detiene un espacio y continua
    print(letras)
# ////////////////////////////////////////////////////////////////////////////////
# While regresivo
numero = 10
while numero >= 0:
    print(numero)
    numero -= 1

# Numeros pares
numero = 50
while numero >= 0:
    if numero % 2 == 0:
        print(f"{numero} Par")
        numero -= 1
    else:
        numero -= 1
        continue

# Imprime los numeros de una lista que sean mayot a 0
lista_numeros = [4, 5, 8, 7, 6, 9, 8, 2, 4, 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]
for numero in lista_numeros:
    if numero > 0:
        print(numero)
    else:
        break
