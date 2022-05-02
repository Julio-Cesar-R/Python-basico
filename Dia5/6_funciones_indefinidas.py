def suma(*args):
    suma_total=0
    for n in args:
        suma_total=suma_total+n
    print(suma_total)


suma(1,2,3,4,5,6)

def suma_listas(lista):
    return sum(lista)


print(suma_listas([1,2,3,4,5,6]+[2,3]))


def suma_cuadrados(*args):
    sumaa = 0
    cuadrado = 0
    for n in args:
        cuadrado=n**2

        sumaa= sumaa+cuadrado
    return sumaa

print(suma_cuadrados(1,2,3))

def suma_absolutos (*args):
    sumat=0
    for n in args:
        num_neg=0
        if n<0:
            num_neg= n*-1
            sumat=sumat+num_neg

        else:
            sumat=sumat+n
    return sumat
print(suma_absolutos(-1,-4,3))


def numeros_persona(nombre,*args):
    suma_numeros=0
    suma_numeros=sum(args)
    return f"{nombre}, la suma de tus números es {suma_numeros}"

print(numeros_persona("juan",1,2,3))