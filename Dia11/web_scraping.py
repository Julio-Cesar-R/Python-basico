'''
Sirve para extraer informacion de sitios web y almacenarlos
en objetos de Python
-Es importante verificar que el sitio web de este tipo de permisos
o podria bloquear tu ip

Instalar modulos en consola
beautifulsoup4
lxml
requests
'''
import requests
import bs4
#BUSQUEDA POR ETIQUETAS
resultado=requests.get("https://escueladirecta-blog.blogspot.com/2022/03/python-pep8-que-es-y-cuales-son-sus.html")#obtener codigo fuente de una pagina web
#print(resultado.text)#mostrarlo con .text
sopa=bs4.BeautifulSoup(resultado.text,"lxml")#lo transforma para poder hacer busqueda

#print(sopa.select("a")[0].getText())#Busqueda de etiqueta,Usar len para ver cuantas existen
                            #Se define el numero de la lista y la posicion del numero de etiqueta que se quiere extraer


#Recorre una lista en la que estan asignados los valores de "p"
lista=[]
parrafo_especial=(sopa.select("p"))
for e in range(len(parrafo_especial)):
    #print(parrafo_especial[e].getText())
    lista.append(parrafo_especial[e].getText())
#print(lista[6])

#///////////////////////////////////
resultado1=requests.get("https://www.escueladirecta.com/courses")
sopa1=bs4.BeautifulSoup(resultado1.text,"lxml")
clase=sopa1.select(".course-listing-subtitle ")

#for n in clase:
    #print(n.getText())#imprimir con ciclo for

#///////////////////////////////////////////////////////////////////////////////////////////
#BUSCAR IMAGENES

resultado2=requests.get("https://www.escueladirecta.com/courses")
sopa2=bs4.BeautifulSoup(resultado2.text,"lxml")

imagenes=sopa2.select(".course-box-image")#[0]["src"]
print(imagenes)
#verificar cual es la imagen que buscas y en donde se encuentra, comienza buscando "img"

#GUARDAR IMAGENES
#imagenes_curso=requests.get(imagenes)#almacena la imagen
#print(imagenes_curso.content)#Muestra la imagen en binario

imagenes_curso=""
impresion=""
contador=0
for i in imagenes:
    impresion=sopa2.select(".course-box-image")[contador]["src"]
    #print(impresion)
    imagenes_curso=requests.get(impresion)
    f = open(f"imagen_curso{contador}.jpg", "wb")  # ruta y tipo de apertura del archivo
    f.write(imagenes_curso.content)
    f.close()
    contador+=1




