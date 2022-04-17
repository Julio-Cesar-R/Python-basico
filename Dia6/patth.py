from pathlib import Path
'''
base=Path.home()
print(base)#directorio principal de la computadora
guia=Path("barcelona","sagrada_familia.txt")#crea directorios
print(guia)

link_p=Path(base,"kaiser",guia)#crear path de paths
print(link_p)

guia2=link_p.with_name("chihuahua.txt")#with name reemplaza el nombre del archivo
print(guia2)

print(link_p.parent)#muestra la carpeta mas cercana del archivo
print(link_p.parent.parent)#muestra la carpeta anterior a la elegida
print("\n")

directorio=Path("C:/Users/julio/OneDrive/Documentos/Cesar/Curso python Docs/Día 6/Archivos_directorios/Europa")
for txt in Path(directorio).glob("**/*.txt"):#busqueda de archivos en carpetas con un * //busca manera global **/*
    print(txt)
print("\n")
'''

guia3=Path("Europa","España","Barcelona","Sagrada_Familia.txt")
en_europa=guia3.relative_to(Path("Europa"))#coincidencias en los directorios
en_espania=guia3.relative_to(Path("Europa","España"))

print(en_europa)
print(en_espania)
#/////////////////////////////////////////////////////////
from pathlib import Path
ruta_base=Path.home()

from pathlib import Path
ruta=Path("Curso Python/Día 6/practicas_path.py")

from pathlib import Path
ruta=Path(Path.home(),"Curso Python/Día 6/practicas_path.py")