#Buscar la lista de excepciones de todos los tipos distintos
'''def suma():
    num1=int(input("ingresa el primer numero"))
    num2=int(input("ingresa el segundo numero"))
    print(f"El resultado de la suma = "+3)
    print("gracias por sumar")


try:
    #Codigo que se va a probar
    suma()
except TypeError:
    #Codigo que se ejecuta si hay un error
    print("Estas intentanto concatenar tipos distintos")
except ValueError:
    print("se ingreso un dato de tipo incorrecto")
else :
    #Codigo si no hay un error
    print("Hiciste todo bien")
finally:
    #el codigo que se va a ejecutar de todas formas
    print("eso es todo")'''

def numero():
    while True:
        try:
            numero=int(input("ingresa un numero"))
        except:
            print("ese no es un numero")
        else:
            print("todo salio bien")
            break#Termina el ciclo

numero()
#//////////////////////////////////////////////////////////////////////////////
def suma(num1, num2):
    try:
        print(num1 + num2)
    except:
        print("Error inesperado")


def cociente(num1, num2):
    try:
        print(num1 / num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")


def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")
