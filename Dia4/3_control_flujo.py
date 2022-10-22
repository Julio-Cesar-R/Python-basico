# Condicionales

# Condicion con variable booleanna
condicion = True
if condicion:
    print("la condicion es verdadera")
else:
    print("la condicion es falsa")

if 5 > 55:
    print("Condicion verdadera")
else:
    print("condicion falsa")
# Condicion con valores asignados por el usuario
numero1 = int(input("Ingresa un numero :"))
numero2 = int(input("ingresa otro numero :"))
if numero1 == numero2:
    print("los numeros son iguales")
elif numero1 > numero2:
    print(f"el numero {numero1} es mayor que el numero {numero2}")
else:
    print(f" el numero {numero1} es menor al numero {numero2}")

# Ejemplos de conndiciones
if 10 == 1:
    print("es igual")
elif 100 < 15:
    print(" es verdad")
else:
    print("nada es verdadero")

if True:
    print("genial")
# Ejemp1
mascota = "gato"
if mascota == "perro":
    print(f"tu mascota es un {mascota}")
elif mascota == "gato":
    print(f"tu mascota es un {mascota}")

else:
    print("no se que animal tienes")
# Ejemp 2
edad = 19
calificacion = 9
sueldo = 1000000
if edad < 18:
    print("eres menor de edad")
    if calificacion >= 7:
        print("tu promedio es aprobatorio")
    else:
        print("estas reprobado")
else:
    print("usted es mayor de edad")
    if sueldo >= 10000:
        print("ganas bien")
    else:
        print("eres algo pobre")
# /////////////////////////////////////////////////////////////////
# Ejemp3
num1 = input("Ingresa un número:")
num2 = input("Ingresa otro número:")
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
elif num2 == num1:
    print(f"{num1} y {num2} son iguales")
# Ejemp4
edad = 16
tiene_licencia = False
if edad >= 18:
    if tiene_licencia == True:
        print("Puedes conducir")
    elif edad >= 18 and tiene_licencia == False:
        print("No puedes conducir. Necesitas contar con una licencia")
    else:
        print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    print("Necesitas ser mayor de edad")

# Ejemp5
edad = 16
tiene_licencia = False
if (edad >= 18) and (tiene_licencia == True):
    print("Puedes conducir")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

# Ejemp6
habla_ingles = True
sabe_python = False
if habla_ingles == True:
    if sabe_python == True:
        print("Cumples con los requisitos para postularte")
    else:
        print("Para postularte, necesitas saber programar en Python")

else:
    print("Para postularte, necesitas tener conocimientos de inglés")

# elif(habla_ingles==False and sabe_python==False):
#   print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
