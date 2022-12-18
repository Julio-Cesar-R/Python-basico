def cadenas_fortmato():

    # *Saltos de linea
    print("Línea 1\nLínea 2\nLínea 3")
    # * Tabulador con saltos de linea
    print("A\tB\tC\nD\tE\tF\nG\tH\tI\n")
    # * Escribir barras diagonales
    print("Barra Normal: /\nBarra Invertida:\\")


def cadenas_listas():
    """
    Ingresar cadenas de texto a listas
    """
    palabra = "algo algo2 algo3 algo4"
    lista = []  # Divide una cadena de caracteres en una lista por medio de espacios
    for n in palabra.split():
        lista.append(n)
    print(lista[0])

    print(palabra[9])  # muestra la posicion de el string entre los corchetes

    print(len(palabra))  # Cantidad de caracteres en una cadena
    print(
        palabra.count("al")
    )  # muestra la cantidad de veces que se repite un patron o letra en la cadena
    print(
        f"El caracter se encontro en la posicion {palabra.find('2')}"
    )  # posicion del caracter encontrado
    print(palabra.upper())
