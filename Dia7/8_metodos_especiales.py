lista = [1, 2, 3, 4, 5]
print(len(lista))


class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):  # metodo especial que devuelve una cadena literal
        return f"El autor es {self.autor} el album es {self.titulo} y contiene {self.canciones} canciones"

    def __len__(
        self,
    ):  # se define que el largo sera igual a cantidad de canciones cada vez que se solicite mediante una instancia
        return self.canciones

    def __del__(self):
        print("se ha eliminado este objeto")


mi_cd = CD("Pink Floid", "The wall", 24)
print(
    mi_cd
)  # gracias al metodo especial podemos retornar la informacion de la instancia creada __str__
print(len(mi_cd))  # se pide el largo del objeto

del mi_cd  # sirve para eliminar una innstancia
# /////////////////////////////////////////
class Libro:
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

    def __len__(self):
        return self.cantidad_paginas

    def __del__(self):
        return "se ha eliminado el libro"
