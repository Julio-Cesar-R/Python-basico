# Manejo de cadenas de caracteres
def cadenas_de_texto():
    """
    En este metodo se muestran las diferentes
    formas en las que se puede imprimir una variable de tipo cadena

    """
    texto = "Kaiser Fox"
    print(f"hola  a todos {texto}")

    var = 1
    nom = "texto"
    print(f"Hola esto es un {nom} numero {var}")

    num1 = 1
    num2 = 4
    print(f" la suma de {num1} y {num2} es {num1+num2}")


def cadena_posicion():
    """
    Muestra las posiciones de un texto dentro de una cadena
    """
    texto = "Kaiser Fox"
    # Primera posicion de la cadena
    a = texto[0]
    print(a)

    # Primeras tres posiciones
    print(texto[0:3])

    # Cadena separada por ""
    print(texto.split())


def modificar_cadenas():
    """
    Modifica el texto de una cadena (mayusculas, minusculas y titulos)
    """
    texto = "Kaiser Fox"
    # Convertir una cadena en mayusculas
    print(texto.upper())

    # Convertir una cadena a minusculas
    print(texto.lower())

    # Convertit una cadena en un titulo
    print(texto.title())


def cadenas_listas():
    """
    Ingresa una cadena de texto dentro de una cadena
    """
    texto = "Kaiser Fox"
    # Asignar una cadena de caracteres a una lista
    lista = texto.split()
    print(lista[1])

    # Asignar una cadena con el ciclo for
    nueva_lista = []
    for n in lista:
        nueva_lista.append(f"k{n}")

    print(nueva_lista)

    # Ingresa una cadena de texto separada por espacios dentro de una lista
    list2 = list(texto.split())
    print(list2)


def cadenas_imprimir():
    """
    Muestra las diferentes formas en las que
    se puede imprimir una cadena de caracteres
    """
    # Imprimir una cadena de caracter simple
    print("hola mundo")
    # Incluir comillas en una cadena
    print("'Esto esta entre comillas'")
    # Suma de dos  numeros
    print(3 + 333)
    # Cadena literal de numeros
    print("3+333")

    # Usos de la barra invertida
    print(
        'estas son "otras comillas"' + " " + "y su espacio"
    )  # una forma de poner comillas y concatenar un espacio
    print("Esta es una linea\nY esta es otra linea")  # salto de linea
    print("\t esta es otra linea")  # tabulador
    print(
        "this isn't a number"
    )  # toma el siguiente caracter como un caracter incluso si son comillas
    print(
        "este signo \\ es una barra ivertida"
    )  # sirve para imprimir una barra invertida
