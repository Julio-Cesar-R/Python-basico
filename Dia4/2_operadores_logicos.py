mibool = (4 < 5) and (
    "perro" == "perro"
)  # ambas condiciones deben cumplirse para ser true
print(mibool)

mbol = (10 == 10) or (
    4 == 5
)  # es verddadero siempre que se cumpla una de las dos condiciones
print(mbol)

texto = " esta es un frase de prueba"  # uso del in y el not in
mibool = ("esta" in texto) and ("de" not in texto)
print(mibool)

b = not ("a" == "a")  # busca que la comparacion sea negativa
print(b)
# /////////////////////////////////////////////////////////
num1 = 36
num2 = 72 / 2
num3 = 48
mi_bool = (num1 > num2) and (num1 < num3)

num1 = 36
num2 = 72 / 2
num3 = 48
mi_bool = (num1 > num2) or (num1 < num3)

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = (palabra1 not in frase) and (palabra2 not in frase)
