from pathlib import Path
from pathlib import (
    PureWindowsPath,
)  # direcion pura de windows, trasnforma a formato windows

carpeta = (
    Path(
        "/Users/julio/OneDrive/Documentos/Cesar/Curso python Docs/Día 6/Archivos_directorios"
    )
    / "otro_archivo.txt"
)
# Ruta en mac y linux

ruta_windows = PureWindowsPath(carpeta)
# ruta de windows
print(ruta_windows)

print(carpeta.read_text())  # lee el objeto de tipo path
print(carpeta.name)  # nombre del archivo
print(carpeta.suffixes)  # muestra el tipo de archivo ejem"txt
print(carpeta.stem)  # nombre del archivo sin su extencion
if not carpeta.exists():
    print("este archivo no exise")
else:
    print("este archivo existe")
