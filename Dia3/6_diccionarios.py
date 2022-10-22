# Diccionarios
# Diccionarios
dic = {"clave1": 4, "clave2": 6, "clave3": 5}
print(dic)
print(dic.keys())
print(dic.values())
print(dic["clave1"])

diccionario = {"verde": "green", "rojo": "red", "Amarillo": "Yellow"}
print(diccionario["verde"])

for n in diccionario.keys():
    if n == "verde":
        print(diccionario[n])
    else:
        print("no hay coincidencia")
# reasignar un valor
diccionario["Amarillo"] = "YELLOW"
print(diccionario)
# agregar un nuevo valor
diccionario["Negro"] = "Black"
print(diccionario)
# ////

diccionario = {"d1": "juan", "d2": "perdro"}
print(type(diccionario))
print(diccionario)

resultado = diccionario[
    "d2"
]  # hace la busqueda de la clave mostrando o almacenando unicamente el valor
print(resultado)
cliente = {
    "nombre": "julio",
    "apellido": "rosas",
    "edad": 29,
    "sueldo": 199.7,
    "habilidades": ["programar", "administrar", "grestionar"],
}
print(cliente["habilidades"])

dic = {"c1": 58, "c2": [12, 23, 34], "c3": {"s1": 1, "s2": 2}}
print(dic["c2"][2])  # busca dentro de la lista por posicion
print(dic["c3"]["s2"])  # busca dentro del diccionario dentro del diccionario

dic1 = {"c1": ["a", "b", "c"], "c2": ["d", "e", "f"]}
print(dic1["c2"][1].upper())

dicc = {1: "uno", 2: "dos"}  # agrega clave y valor al diccionario
dicc[3] = "tres"
print(dicc)
dicc[1] = "unoooo"
print(dicc)
print(dicc.keys())  # muestra las claves existentes
print(dicc.values())  # muestra solo los valores
print(dicc.items())  # muestra todo el contenido del diccionario
# /////////////////////////////////////////////////////////////////////////////////////////
mi_dic = {
    "nombre": "Karen",
    "apellido": "Jurgens",
    "edad": 35,
    "ocupacion": "Periodista",
}

mi_dict = {
    "valores_1": {"v1": 3, "v2": 6},
    "puntos": {"points1": 9, "points2": [10, 300, 15]},
}
print(mi_dict["puntos"]["points2"][1])

mi_dic1 = {
    "nombre": "Karen",
    "apellido": "Jurgens",
    "edad": 35,
    "ocupacion": "Periodista",
}
mi_dic1["edad"] = 36
mi_dic1["ocupacion"] = "Editora"
mi_dic1["pais"] = "Colombia"
