#apartir de python 3.10
codigo="n1"

match codigo:
    case "n1":
        print("Nokia")
    case "n2":
        print("samsung")
    case _:
        print(" no es ninguno de los anteriores")

client={"nombre":"kaiser","edad":29,"ocupacion":"desarrollador"}

pelicula={"titulo":"matrix","ficha_tecnica":{"protagonista":"keanu reves", "director":"lana y lili"}}

elementos=[client,pelicula,"algo"]

for e in elementos:
    match e:
        case  {"nombre":nombre,"edad":edad,"ocupacion":ocupacion}:
            print("es un cliente")
            print(nombre,edad,ocupacion)

        case  {"titulo":titulo,"ficha_tecnica":{"protagonista":protagonista,"director":director}}:
            print("es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print("no se que sea")

