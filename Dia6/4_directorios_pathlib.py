
from pathlib import Path

carpeta=Path("C:/Users/julio/OneDrive/Documentos/Cesar/Curso python Docs/Día 6/Archivos_directorios")
#Ruta en mac y linux
archivo=carpeta/"otro_archivo.txt"#se crea la ruta y se almacena
mi_archivo=archivo.open()
print(mi_archivo.read())
mi_archivo.close()

carpeta=Path("/Users/julio/OneDrive/Documentos/Cesar/Curso python Docs/Día 6/Archivos_directorios")/"otro_archivo.txt"
#Ruta en mac y linux
carpeta1=carpeta.open()
print(carpeta1.read())
carpeta1.close()



