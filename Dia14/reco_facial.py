#Instalar visual studio con c++
from cv2 import cv2
import face_recognition as fr

#cargar imagenes
foto_control=fr.load_image_file("foto1.jpg")
foto_prueba=fr.load_image_file("foto4.jpg")

#Pasar imagenes a RGB
foto_control=cv2.cvtColor(foto_control,cv2.COLOR_BGR2RGB)
foto_prueba=cv2.cvtColor(foto_prueba,cv2.COLOR_BGR2RGB)

#Localizar cara control
lugar_cara1=fr.face_locations(foto_control)[0]#Lugar de la foto donde hay un rostro
cara_codificada1=fr.face_encodings(foto_control)[0]

#Localizar cara prueba
lugar_cara2=fr.face_locations(foto_prueba)[0]#Lugar de la foto donde hay un rostro
cara_codificada2=fr.face_encodings(foto_prueba)[0]

#Mostrar rectangulos
cv2.rectangle(foto_control,
              (lugar_cara1[3],
              lugar_cara1[0]),(lugar_cara1[1],#cordenadas
              lugar_cara1[2]),
              (0,255,0),#Color RGB
              2)#Borde de linea
cv2.rectangle(foto_prueba,
              (lugar_cara2[3],
              lugar_cara2[0]),(lugar_cara2[1],#cordenadas
              lugar_cara2[2]),
              (0,255,0),#Color RGB
              2)#Borde de linea


#Realizar comparacion
resultado=fr.compare_faces([cara_codificada1],cara_codificada2)#0.6)Recibe una lista y una foto y la distancia a aceptara la comparacion
print(resultado)

#Medida de la distancia
distancia=fr.face_distance([cara_codificada1],cara_codificada2)
print(distancia)#debe ser menor a 0.6


#Mostrar resultado
cv2.putText(foto_prueba,
            f"Coincidencia= {resultado} Distancia= {distancia.round(2)}",
            (50,50),
            cv2.FONT_HERSHEY_DUPLEX,
            1,
            (0,255,0),
            2)

#Mostrar imagenes
cv2.imshow("Foto control",foto_control)
cv2.imshow("Foto prueba",foto_prueba)

#Mantener programa abierto
cv2.waitKey(0)