def tres_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            print(lista.index(n))
            return True

        else:
            pass
    return False
res=tres_cifras([30,13,10])
print(res)

def tres_cifra(lista):
    lista_def = []
    for n in lista:
        if n in range(100,1000):
            lista_def.append(n)
        else:
            pass
    return lista_def

res=tres_cifra([300,190,100])
print(res)

#///////////////////////////////////////////////
def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n<0:
           return False

        else:
            pass
    return True



lista_numeros = [1,-50,502,-5000,755,600,33,61]
print(todos_positivos(lista_numeros))


def suma_menores(lista_numeros):
    suma=0
    for n in lista_numeros:
        if n in range(1 ,1000):
            suma= suma +n
        else:
            pass
    return suma

def cantidad_pares(lista_numeros):
    suma=0
    for n in lista_numeros:
        if n % 2==0:
            suma= suma +n
        else:
            pass
    return suma

print(cantidad_pares([1,2,3,4]))

lista_numeros = [1, 50, 502, 5000, 755, 600, 33, 61]


def cantidad_pares(lista_numeros):
    cantidad = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            cantidad += 1
        else:
            pass
    return cantidad