from cv2 import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime


#Crear base de datos
ruta="Empleados"
mis_imagenes=[]
nombres_empleados=[]
lista_de_empleados=os.listdir(ruta)


for nombre in lista_de_empleados:
    imagen_actual=cv2.imread(f"{ruta}\{nombre}")
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])


# codificar imagenes
def codificar(imagenes):

    # crear una lista nueva
    lista_codificada = []

    # pasar todas las imagenes a rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # codificar
        codificado = fr.face_encodings(imagen)[0]

        # agregar a la lista
        lista_codificada.append(codificado)

    # devolver lista codificada
    return lista_codificada

def registrar_ingresos(persona):
    f = open('registro.csv', 'r+')
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')

lista_empleados_codificada= codificar(mis_imagenes)#esta es la lista chida



#Tomar una foto con camara web
captura=cv2.VideoCapture(0,cv2.CAP_DSHOW)


#Leer imagen de la camara en dos variables
exito,imagen =captura.read()
if not exito:
    print("no se ha podido tomar la captura")
else:
    #Reconocer cara en captura
    cara_captura=fr.face_locations(imagen)
    #Codificar cara capturada
    captura_cara_codificada=fr.face_encodings(imagen,cara_captura)
    #Buscar coincidencias

    for caracodif, caraubic in zip(captura_cara_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)
        print(coincidencias)
        print(distancias)

        indice_coincidencia=numpy.argmin(distancias)
        #Mostrar coincidencias
        if distancias[indice_coincidencia]>0.6 :#coincidencia es cuando es mayor a este numero en el indice_coincidencia
            print("No coincide con ningun empleado")
        else:
            #Buscar el nombre del empleado buscado
            nombre=nombres_empleados[indice_coincidencia]

            #Mostrar rectangulo
            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_ITALIC, 1, (255, 2555, 255), 2)

            registrar_ingresos(nombre)

            #Mostrar imagen
            cv2.imshow("Immagen web",imagen)
            #mantener ventana abierta
            cv2.waitKey(0)






