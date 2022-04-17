'''
en este modulo ponemos aprueba
la velocidad de ejecucion de dos codigos
que hacen lo mismo
'''
'''import time
def ciclo_for(numero):
    lista=[]
    for n in range (1,numero+1,1):
        lista.append(n)
    return lista

def ciclo_while(numero):
    lista=[]
    contador=1
    while contador<=numero:
        lista.append(contador)
        contador+=1
    return lista
inicio=time.time()
ciclo_for(150000)
final=time.time()
prueba_tiempo1=final-inicio
print(prueba_tiempo1)

inicio=time.time()
ciclo_while(150000)
final=time.time()
prueba_tiempo2=final-inicio
print(prueba_tiempo2)

mayor=(max(prueba_tiempo1,prueba_tiempo2))
menor=(min(prueba_tiempo1,prueba_tiempo2))
res=mayor-menor
print(f"la diferencia de tiempos es de {res}")'''


import timeit



declaracion='''
ciclo_for(100)'''
mi_setup='''
def ciclo_for(numero):
    lista=[]
    for n in range (1,numero+1,1):
        lista.append(n)
    return lista'''

duracion=timeit.timeit(declaracion,mi_setup,number=100000)
print(duracion)

declaracion2='''
ciclo_while(100)'''
mi_setup2='''
def ciclo_while(numero):
    lista=[]
    contador=1
    while contador<=numero:
        lista.append(contador)
        contador+=1
    return lista
'''
duracion2=timeit.timeit(declaracion2,mi_setup2,number=100000)
print(duracion2)