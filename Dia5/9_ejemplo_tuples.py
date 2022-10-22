informacio_cafe = [("capuchino", 2000), ("spresso", 400), ("olla", 1)]
for (
    cafe,
    precio,
) in (
    informacio_cafe
):  # dos variables para almacenar las tuplas tambien funciona con diccionarios
    print(precio)


def precio_mayor(lista_cafe):
    """
    Esta funcion recibe una tupla  en el cual determinara
    el precio mayor y guardara el nombre del cafe y precio para mostrarlo
    """
    precio_mayor = 0
    nombre_cafe = ""
    for nombre, precio in lista_cafe:
        if precio > precio_mayor:
            precio_mayor = precio
            nombre_cafe = nombre
        else:
            pass

    return (nombre_cafe, precio_mayor)


print(precio_mayor(informacio_cafe))
cafe, precio = precio_mayor(
    informacio_cafe
)  # reasignamos el valor a otras dos variables
print(f"el cafe mas caro es {cafe} con un precio de {precio} pesos")
