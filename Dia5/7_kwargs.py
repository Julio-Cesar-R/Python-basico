"""
def sum(**kwargs):
    return type(kwargs)

print(sum(a=1))

def suma1(**kwargs):
    sumat=0
    for clave,valor in kwargs.items():
        print( f"{clave} = {valor}")
        sumat=sumat+valor
    return sumat


print(suma1(a=1, b=2, c=3))
"""


def prueba(num1, num2, *args, **kwargs):
    res = 0
    res2 = 0
    res3 = 0

    for arg in args:
        res2 = res2 + arg

    for clave, valor in kwargs.items():
        res = res + valor

    res3 = num1 + num2 + res + res2
    print(res3)


argu = [4, 1]
dic = {"a": 1, "b": 2, "c": 4}
prueba(2, 4, *argu, **dic)
# ////////////////////////////////////////////////////////////////////////////
def cantidad_atributos(*args):
    contar = 0
    for n in args:
        contar = contar + 1
    return contar


print(cantidad_atributos(1, 2, 3, 4, 5))


def cantidad_atributos(**kwargs):
    contar = 0
    for n in kwargs:
        contar = contar + 1
    return contar


def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista


def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}")
    for nombre_argumento, valor_argumento in kwargs.items():
        print(f"{nombre_argumento}: {valor_argumento}")


describir_persona("julio", a=1, b=2)
