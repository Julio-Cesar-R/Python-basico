import os
import shutil  # mover archivos


print(os.getcwd())  # imprime el directorio atual del archivo.py
archivo = open("curso.txt", "w")  # creara el archivo en el directorio actual
archivo.write("text de prueba")
archivo.close()
print(os.listdir())  # mustra los archivos en el directorio actual

archivo_leer = open("curso.txt")
print(archivo_leer.read())
archivo_leer.close()
# shutil.move("curso.txt","C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Curso python Docs\\Dia 9")
# mueve el archivo a la direccion dada
# os.unlink("ARCHIVO","RUTA") SIRVE PARA ELIMINAR UN ARCHIVO EN UNA RUTA DADA
# os.mkdir() ELIMINA UNA CARPETA
# shutil.rmtree("RUTA")#elimina carpeta y sub carpetas y archivos CUIDADOO
"""
IMPORTAREMOS EN SIMBOLOS DE SISTEMA
LA LIBRERIA "send2trash"
"""
import send2trash

# send2trash.send2trash("curso.txt")#Mueve el archivo a la papelera

"""
walk recorre todas las carpetas y archivos de una ruta dada
"""
# print(os.walk("C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Curso python Docs"))
ruta = "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Curso python Docs"
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta {carpeta}")
    print("las subcarpetas son: ")
    for sub in subcarpeta:
        print("\t" + sub)
    print("Los archivos son:")
    for arc in archivo:
        if arc.startswith("Decoradores") or arc.endswith(
            "pdf"
        ):  # busqueda por inicio o termino del mobre del archivo
            print("\t" + arc)
