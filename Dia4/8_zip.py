nombre = ["Kaiser", "Luis", "Lala"]
edad = [39, 30, 25]
ciudades = ["Lima", "Mexcio", "Argentina"]
juntar = list(zip(nombre, edad, ciudades))
print(juntar)

for nom, ed, ciu in juntar:
    print(f"Nombre: {nom} Edad: {ed} y vive en {ciu}")

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
juntar = list(zip(paises, capitales))
for pai, cap in juntar:
    print(f"La capital de {pai} es {cap}")

marcas = ["algo", "algo1", "algo2"]
productos = ["pro1", "pro2", "pro2"]
mi_zip = list(zip(marcas, productos))

print(mi_zip[0][1])

espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espaniol, portugues, ingles))
