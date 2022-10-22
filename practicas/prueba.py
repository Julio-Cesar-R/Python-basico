def maximo_dos_numeros(n1: int, n2: int):

    """

    :param n1: Numero entero
    :param n2: Numero entero
    :return: Mayo de los dos numeros
    """

    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    elif n1 == n2:
        return n1


resultado = maximo_dos_numeros(34, 34)


# print(resultado)


def maximo_tres_numeros(n1: int, n2: int, n3: int):
    """

    :param n1: Numero entero
    :param n2: Numero entero
    :param n3: Numero entero
    :return: Mayor de los tres numeros
    """

    """
    Algoritmo
    a>b>c
    b>c
    a>c
    """
    var1 = maximo_dos_numeros(n1, n2)
    if var1 > n3:
        return var1
    elif n3 > var1:
        return n3
    elif n3 == var1:
        raise Exception("Los numeros son iguales")


resul = maximo_tres_numeros(3, 2, 1)
print(resul)


def max_def(*args):
    """

    :param args: n numero de integers
    :return: numero meyor
    """
    maximo = max(args)

    """
    Algoritmo
    ((maximo==n) True != n+1)-->((maximo==n) True != n+1)

    """
    for n in args:
        if maximo == n:
            posicion = args.index(n)

    return posicion + 1, maximo


posicion, mayor = max_def(1, 111, 3, 4, 5, 6, 7111, 8, 9)


print(posicion)


a = "juanito peralta"
inverso = "".join(reversed(a))
# print( inverso)


def inverso(cadena):
    """

    :param cadena:
    :return: Inversion de caracteres
    """
    inverso_cad = ""
    i = len(cadena) - 1
    print(i)
    while i >= 0:
        inverso_cad += cadena[i]

        i -= 1

    return inverso_cad


print(inverso("Julio Cesar Rosas Perez"))


def es_palindromo(palabra):
    """
    Esta funcion verifica si la palabra ingresada es un palindromo
    :param cadena:
    :return: True or false
    """
    if palabra == inverso(palabra):
        return True
    else:
        return False


print(es_palindromo("ani"))


def coincidencias(lista1, lista2):
    for n in lista1:
        if n in lista2:
            return True
    else:
        return False


print(coincidencias([1, 2, 3], [6, 4, 5]))

print("imprimir caracter")


def caracter(caracter, repeticiones):
    return caracter * repeticiones


print(caracter("*", 50))


print("Histograma")


def histograma(lis1):
    """

    :param lis1:

    :return: Histograma
    """
    for n in lis1:
        print(caracter("*", n))


print(histograma([4, 9, 7]))
