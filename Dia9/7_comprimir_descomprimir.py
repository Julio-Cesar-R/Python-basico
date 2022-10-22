"""
MODULO ZIPFILE
"""
import zipfile

# COMPRIMIR ARCHIVOS
"""mi_zip= zipfile.ZipFile("Archivo comprimido.zip","w") #(nombre del nuevo zip,tipo de apertura de archivo)
mi_zip.write("mi_texto_A.txt")
mi_zip.write("mi_texto_B.txt")
mi_zip.close()"""

# DESCOMPRIMIR
"""abrir_zip= zipfile.ZipFile("Archivo comprimido.zip","r")#archivo que va a descomprimir y tipo de apertura
abrir_zip.extractall()"""

"""
MODULO SHUTIL
"""
import shutil

# COMPRIMIR
"""ruta="C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Curso python Docs\\Dia 9\\Ejercicio"
archivo_destino="carpeta comp"#nombre del archivo zip
shutil.make_archive(archivo_destino,"zip",ruta)
#ESTE ARCHIVO SE GUARDA EN DONDE ESTA LA RUTA ACTUAL DEL PROYECTO
"""


# DESCOMPRIMIR
shutil.unpack_archive(
    "carpeta comp.zip", "extracccion_terminada", "zip"
)  # (carpeta a descomprimir,ruta y nombre de la nueva carpeta,formato)
shutil.unpack_archive(
    "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Curso python Docs\\Dia 9\\Proyecto+Día+9.zip",
    "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Curso python Docs\\Dia 9\\Proyecto 9",
    "zip",
)
