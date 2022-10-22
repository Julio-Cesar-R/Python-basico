from pathlib import Path

ruta = Path(
    "C:/Users/julio/OneDrive/Documentos/Cesar/Curso python Docs/Día 6/Archivos_directorios/otro_archivo.txt"
)


def abrir_leer(ruta):
    return Path.read_text(ruta)


print(abrir_leer(ruta))


def abrir_leer(archivo):
    archivo = open(archivo)
    return archivo.read()


def sobrescribir(archivo):
    archivo1 = open(archivo, "w")
    archivo1.write("Contenido eliminado")


def registro_error(archivo):
    archivo1 = open(archivo, "a")
    archivo1.write("se ha registrado un error de ejecución")
    archivo1.close()
