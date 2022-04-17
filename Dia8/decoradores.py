#igualamos el reesultado de una funcion para mandar llamar otra funcion
'''def cambiar_letras(tipo):

    def mayusculas(palabra):
        return palabra.upper()

    def minuscula(palabra):
        return palabra.lower()

    if tipo == "may":
        return mayusculas
    elif tipo == "min":
        return minuscula


argumento=cambiar_letras("may")
print(argumento("chinga"))
'''
def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print("adios")
    return otra_funcion
#@decorar_saludo #aqui es como se llama a la decoracion con el nombre dela funcion
def mayusculas(palabra):
    print (palabra.upper())

def minuscula(palabra):
    print( palabra.lower())
minuscula_decorada=decorar_saludo(minuscula)#Otra forma de imprimir decorador
mayuscula_decorada=decorar_saludo(mayusculas)
mayusculas("viva mexico")
minuscula_decorada("VIVAN TODOS")#aqui se manda llamar
minuscula("HIIIIIIIIII")
mayuscula_decorada("gureto daze")

