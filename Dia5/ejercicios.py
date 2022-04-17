def devolver_distinto(*args):
    '''
    Ejercicio 1
    '''
    res=0
    res=sum(args)
    print(res)
    mayor=0
    mayor=max(args)
    menor=0
    menor=min(args)
    intermedio=0
    for n in args:
        if n!= mayor and n!=menor:
            intermedio=n


    if res>15:
        return mayor
    elif res<10:
        return menor
    elif res>=10 and res<=15:
        return intermedio
print(f"el numero es {devolver_distinto(11,2,3)}")

def reacomodar(palabra):
    '''
        Ejercicio 2
    '''

    pal=sorted(palabra)

    lista= list(pal)
    print( lista)
    nueva_lista=[]
    for n in lista:
        if n not in nueva_lista:
            nueva_lista.append(n)
        else:
            pass
    return nueva_lista

print(reacomodar("juliooaaaaa"))
def no_repe(palabra):
    '''
        Ejercicio 2
    '''
    set_pala=set(palabra)
    print(sorted(set_pala))
no_repe("juliooooaaaa")


def num_cero(*args):
    '''
     Ejercicio 3
    '''
    contador=0
    for nun in args:
        if contador+1==len(args):
            return False
        elif args[contador]==0 and args[contador+1]==0:
            return True
        else:
            contador+=1
    return False

print(num_cero(0,9,0,6,4,4,0))

def contar_primos(numero):
    nueva_lista=[]
    iteracio=0
    lista=list(range(3,numero+1))
    print(lista)
    for n in lista[::2]:
        if n%n==0:
            break
        else:
            nueva_lista.append(n)

    print(nueva_lista)


contar_primos(20)
