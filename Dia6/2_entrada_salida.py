'''
Manipulacion de archivos txt
'''
archivo=open("prueba.txt") #nombre del archivo
#print(archivo.read())#mostrar contenido del archivo
#una_linea=archivo.readline()#muestra la primera linea del archivo
#print(una_linea)

#una_linea=archivo.readline()#si se repite esta linea de codigo se imprimiran las lineas consecutivas en el archivo
#print(una_linea.rstrip())#quita el salto de linea que se da por default
#una_linea=archivo.readline()
#print(una_linea)


#for l in archivo:#este ciclo toma como referencia la cantidad de lineas en el archivo
 #   print(f"aqui dice: {l}")
todas_lineas= archivo.readlines()# ingresa las lineas del archivo en una lista
print(todas_lineas)

archivo.close()#este metodo cierra el archivo para no saturar el espacion de memoria

#//////////////////////////////////////////////////////////////////////////////////
archivo=open("texto.txt")
print(archivo.read())

archivo=open("texto.txt")
print(archivo.readline())

archivo=open("texto.txt")
linea=archivo.readlines()
print(linea[1])