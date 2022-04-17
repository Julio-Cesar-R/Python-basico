from pathlib import Path
from os import system
ruta_base=Path("C:/Users/julio/OneDrive/Documentos/Cesar/Curso python Docs/Día 6/Proyecto 6/Recetas")
def continuar():
    desicion_final=input("¿Quieres regresar al menu principal? s/n: ")
    if desicion_final=="s"or desicion_final=="S":
        system("cls")
        menu(ruta_base)
    elif desicion_final=="n"or desicion_final=="N":
        exit()
    else:
        print("La respuesta que diste no fue clara")
        system("cls")
        continuar()
def contar_recetas(ruta):
    contador=0
    for txt in ruta.glob("**/*txt"):
        contador+=1
    return contador
def mostrar_cat_rec(ruta):
    print("Bienvendio estas son las categorias".upper())
    for carpeta in Path(ruta).iterdir():
        print(carpeta.name.upper())

        for txt in carpeta.glob("**/*txt"):
                print("-"+txt.stem)
def leer_receta(ruta,categoria,receta):
    visualizar_receta=Path(ruta,categoria,receta+".txt")
    print(Path.read_text(visualizar_receta))
def crear_receta(ruta,categoria,receta,texto):
    ruta_nueva=Path(ruta,categoria,receta+".txt")
    crear_receta=open(ruta_nueva,"w")
    crear_receta.write(texto)
    crear_receta.close()
def eliminar_receta(ruta,categoria,receta):
    visualizar_receta=Path(ruta,categoria,receta+".txt")
    Path.unlink(visualizar_receta)
def leer_categoria(ruta,categoria):
    ruta1=Path(ruta,categoria)
    for txt in Path(ruta1).glob("**/*txt"):
            print("-"+txt.stem)
def crear_categoria(ruta,categoria):
    crear_catego=Path(ruta,categoria)
    crear_catego.mkdir(parents=True, exist_ok=True)
def eliminar_categoria(ruta,categoria):
    crear_catego=Path(ruta,categoria)
    crear_catego.rmdir()
def validacion_numero(numero,ruta):
    abecedario="abcdefghijklmnñopqrstuvwxyz"
    abecedario2=abecedario.upper()

    if numero in abecedario or numero in abecedario2 :
        print("Usted no ingreso un numero\n")
        menu(ruta)

    elif numero=="1":
        print("LEER RECETA ")
        categoria=input("Escriba la categoria: ")
        receta=input("Ingrese el nombre de la receta: ")
        leer_receta(ruta,categoria,receta)
        continuar()

    elif numero=="2":
        print("CREAR RECETA")
        categoria = input("Escriba la categoria: ")
        receta = input("Ingrese el nombre de la receta: ")
        descripcion_receta=input("Escriba la receta: ")
        crear_receta(ruta, categoria, receta,descripcion_receta)
        continuar()

    elif numero=="3":
        print("ELIMINAR RECETA")
        categoria = input("Escriba la categoria: ")
        receta = input("Ingrese el nombre de la receta: ")
        eliminar_receta(ruta, categoria, receta)
        continuar()

    elif numero=="4":
        print("LEER CATEGORIA")
        categoria = input("Escriba la categoria: ")
        leer_categoria(ruta, categoria)
        continuar()

    elif numero=="5":
        print("CREAR CATEGORIA")
        categoria = input("Escriba la categoria: ")
        crear_categoria(ruta, categoria)
        continuar()

    elif numero=="6":
        print("ELIMINAR CATEGORIA")
        categoria = input("Escriba la categoria: ")
        eliminar_categoria(ruta, categoria)
        continuar()

    elif numero=="7":
        print("MOSTRAR CATEGORIAS Y RECETAS")
        mostrar_cat_rec(ruta)
        continuar()

    elif numero=="8":
        print("EL PROGRAMA SE HA CERRADO")
        exit()

    else:
        print("El numero que usted igreso esta fuera del rango\n")
        menu(ruta)
def menu(ruta):

    print(f'''Bienvedido al recetario
La cantidad de recetas hasta el momento son {contar_recetas(ruta_base)}
1- Leer receta
2- Crear receta
3- Eliminar receta
4- Leer categoria
5- Crear categoria
6- Eliminar categoria
7- Mostrar categorias y recetas
8- Cerrar programa
''')
    numero_elegido = input("Elija la opcion que desea realizar con numeros:")

    validacion_numero(numero_elegido,ruta)

menu(ruta_base)





