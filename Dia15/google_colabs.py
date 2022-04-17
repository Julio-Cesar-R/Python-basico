'''
En este capitulo exploramos google colaboratory
ejecutando lineas de comando de python
'''
import numpy as np
array_tridim=np.array([[[1,2,3],
                    [4,5,6]],
                    [[7,8,9],
                    [10,11,12]]])

array_unidim=([1,2,3,4,5])

import pandas as pd
datos=pd.DataFrame(array_unidim)
print(datos)
#pandas va de la mano con numpy, es el excel de python

#Crear arrays
uno=np.ones((4,7))#filas y columnas
print(uno)

ceros=np.zeros((2,4,3))
print(ceros)

array_5=np.random.randint(0,10,(3,4))

#Busqueda en STACK OVERFLOW
 #//////////////////////////////////////////////////////////////////
 #PANDAS