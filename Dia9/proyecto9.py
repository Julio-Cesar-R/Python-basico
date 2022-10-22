"""
BUSQUEDA DE ARCHIVOS CON EXPRESIONES REGULARES
"""
import os
import re
import datetime
import time

ruta = "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Curso python Docs\\Dia 9\\Proyecto 9\\Mi_Gran_Directorio\\"
hoy = datetime.date.today()
lista_encontrados = []


inicio = time.time()
print(f"Fecha de busqueda: {hoy}")
print("ARCHIVO         NRO DE SERIE")
walking = os.walk(ruta)
for carpeta, subcarpeta, archivo in walking:

    for sub in subcarpeta:
        pass

    for arc in archivo:
        formato = r"\bN\w{3}-\d{5}"
        nueva_ruta = open(carpeta + "\\" + arc)
        texto_analizar = nueva_ruta.read()
        resultado = re.search(formato, texto_analizar)
        if resultado != None:

            print(arc + "\t" + resultado.group())
            lista_encontrados.append(arc)
            nueva_ruta.close()
print(f"Numeros encontrados: {len(lista_encontrados)}")
final = time.time()
prueba_tiempo1 = final - inicio
print(f"Duracion de la busqueda: {prueba_tiempo1} segundos")
