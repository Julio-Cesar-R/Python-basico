"""
EXPRESIONES REGULARES Y COMO SE DEFINEN
BUSQUEDA
"""
import re  # exportar libreria

texto = "Si necesitas ayuda comunicate con nosotros al  numero(009)-647-8765 por favor"
patron = "a"
busqueda = re.search(patron, texto)  # busqueda con RE- enciuentra la primera aparicion
print(busqueda.span())  # el rango en que se encuentra
print(busqueda.start())  # donde comienza

buscar_todo = re.findall(patron, texto)  # busca todas las coincidencias
print(buscar_todo)  # muestra una lista de todas las coincidencias
print(len(buscar_todo))  # numero de coincidencias

for coincidencia in re.finditer(patron, texto):  # posicion de las coincidencias
    print(coincidencia.start())
print("/" * 50)
print("/" * 50)
"""
CREACION DE EXPRESIONES REGULARES
BUSQUEDA DE ESTRUCTURAS
"""
texto_numero = "comunicate al 555-455-8765 o al siguiente numero 756-345-0000 "
# patron_numero= r"\d\d\d-\d\d\d-\d\d\d\d"
patron_numero = re.compile("(\d{3})-(\d{3})-(\d{4})")  ##cuantificada y agrupados

busqueda_numero = re.search(patron_numero, texto_numero)  # busqueda (patron, texto)
print(busqueda_numero)
print(
    busqueda_numero.group(2)
)  # obtiene solo la busqueda o se define el grupo de busqueda
print("/" * 50)
print("/" * 50)

busqueda_total = re.findall(
    patron_numero, texto_numero
)  # busqueda de todas las coincidencias (patron, texto)
print(busqueda_total)
# /////////////////////////////////////////////////////////////////////////////
"""
EXPRESIONES REGULARES CON TEXTO
"""
print("/" * 50)
print("/" * 50)

clave = input("ingrese una clave no mayor a 8 digitos y no empiece con un numero")
patron1 = r"\D{1}\w{7}"
comparacion = re.search(patron1, clave)
print(comparacion)
if comparacion != None:
    print("clave aceptada")
else:
    print("contraseña no valida")
print("/" * 50)
print("/" * 50)
"""
OPERADORES ESPECIALES
"""
texto1 = "en esta tienda solo abrimos lunes y martes"
buscar = re.search(r"lunes|martes", texto1)  # | es igual a "or"
print(buscar)

buscar2 = re.search(
    r".mos......", texto1
)  # los puntos nos muestas los espacios del texto que no se ven
print(buscar2)

buscar3 = re.search(
    r"^\D{5}", texto1
)  # verifica que la primera posision no sea un numero o cualquier otra
print(buscar3)

buscar4 = re.search(
    r"....\D$", texto1
)  # verifica que la ultima posision no sea un numero o cualquier otra
print(buscar4)

buscar5 = re.findall(r"[^\s]+", texto1)  # excluye los espacios vacios
print(buscar5)
print("".join(buscar5))  # imprime todo junto

# ///////////////////////////////////////////////////////////////

"""
CORREO ELECTRONICO
"""


def verificar_email(email):
    if re.search(r"@\w+\.com", email):
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


verificar_email("algo@algo.com")

"""
VERIFICA QUE UNA CADENA COMIENCE CON UN TEXTO ESPECIFICO
"""


def verificar_saludo(frase):
    patron = r"^hola"
    if re.search(patron, frase):
        print("Ok")
    else:
        print("No has saludado")


verificar_saludo("hola madafakas hola")

# VALIDA UN CODIGO POSTAL
def verificar_cp(cp):
    patron = r"\w{2}\d{4}"
    if re.search(patron, cp):
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")


verificar_cp("DD875")

# correo electronico
# r'@.+\.com$'
