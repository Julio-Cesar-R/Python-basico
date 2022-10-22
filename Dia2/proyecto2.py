nombre = input("¿Cual es tu nombre?:  ")
ventas = float(input("¿cuanto vendiste?: "))
comision = ventas * 13 / 100
print(f"{nombre} usted obtuvo un porcentaje de {round(comision,2)}")
