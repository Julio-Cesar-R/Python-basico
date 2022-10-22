minimo = min(5, 2, 8, 6, 4, 2)
maximo = max(5, 2, 8, 6, 4, 2)
print(f"Menor= {minimo} Mayor= {maximo}")

lista = [5, 2, 8, 6, 4, 2]
print(max(lista))

nombres = ["lala", "kaiser", "zorro"]
print(min(nombres))

nombre = "lala"
print(min(nombre))

dic = {"c1": 999, "c2": 1}
print(min(dic.values()))
# //////////////////////////////////////////////////////////////////////////////////////
lista_numeros = [
    44542247 / 2,
    21310 / 5,
    2134747 * 33,
    44556475,
    121676,
    6654067,
    353254,
    123134,
    55**12,
    611**5,
]
valor_maximo = max(lista_numeros)
lista_numeros = [
    44542247,
    21310,
    2134747,
    44556475,
    121676,
    6654067,
    353254,
    123134,
    552512,
    611665,
]

mini = min(lista_numeros)
maxi = max(lista_numeros)
rango = maxi - mini

diccionario_edades = {
    "Carlos": 55,
    "María": 42,
    "Mabel": 78,
    "José": 44,
    "Lucas": 24,
    "Rocío": 35,
    "Sebastián": 19,
    "Catalina": 2,
    "Darío": 49,
}
edad_minima = min(diccionario_edades.values())
print(edad_minima)
ultimo_nombre = max(diccionario_edades)
print(ultimo_nombre)
