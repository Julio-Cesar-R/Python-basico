from os import system

nombre = input("dime tu nombre: ")
edad = input("dime tu edad: ")
system(
    "cls"
)  # borra el contenido de la consola, configurar Run/debug/configuracion/ marcar opcion de consola de windows
print(nombre)
print(edad)
desicion = input("Deseas apagar la pc S/N")
if desicion == "S":
    print("Apagando sistema")
    system("shutdown /s")  # Comando para apagar la pc
else:
    print("Se ha cancelado el apagado")

arra = ["algo", "algo1", "Algo2"]
