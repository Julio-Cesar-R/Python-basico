import os  # sistema operativo

# ruta=os.getcwd()# obtiene la ruta actual

ruta = os.chdir(
    "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Curso python Docs\\Día 6\\Archivos_directorios"
)
# sirve para ingresar una ruta, no olvidar poner los doble \\ no escribir el nombre del archivo aun

ruta = os.makedirs(
    "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Curso python Docs\\Día 6\\Archivos_directorios\\otra"
)
# crear directorios

archivo = open("otro_archivo.txt")  # nombre del archivo
print(archivo.read())
archivo.close()
# ///////////////////////////////////////////////////////////////

ruta = "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Cursopython\\Python\\Dia6\\prueba.txt"
elemento = os.path.basename(ruta)  # obtiene el nombre del archivo de la ruta dada
elemento2 = os.path.dirname(ruta)  # obtiene el directorio de carpetas
elemento3 = os.path.split(ruta)  # divide la ruta en una lista de dos caracteres
print(elemento)
print(elemento2)
print(elemento3)

os.rmdir(
    "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Curso python Docs\\Día 6\\Archivos_directorios\\otra"
)
# elimina carpeta de un directorio

ruta = open(
    "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Curso python Docs\\Día 6\\Archivos_directorios\\otro_archivo.txt"
)
print(ruta.read())
