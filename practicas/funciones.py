def sumar_algo(*args):
    """
    Esta funcion suma un numero indetermidado de numeros
    y lo almaneca en la variable resultado
    return= resultado
    """
    resultado = 0

    for n in args:
        resultado = resultado + n
    return resultado


def mayor(*args):
    """
    Esta funcion identifica el mayor de los numeros ingresados en un arreglo
    :param args:
    :return: Integer
    """
    mayor = max(args)
    return mayor
