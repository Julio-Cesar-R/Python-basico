class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    balance = 0

    def __init__(self, nombre, apellido, num_cuenta):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nNumero de cuenta {self.num_cuenta}\nDinero disponible: {self.balance}\n "

    def depositar(self, monto):
        self.balance += monto
        print(f"Su deposito fue de {monto}\nDinero disponible {self.balance}\n")

    def retirar(self, monto):
        if self.balance >= monto:
            self.balance -= monto
            print(f"Su retiro fue de {monto}\nDinero disponible {self.balance}\n")
        else:
            print(
                f"Usted no puede retirar esa cantidad ya que no hay dinero suficiente\nMonto disponible {self.balance}"
            )


def crear_cliente():
    num_cuenta = 9999999999999999
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    cliente_cl = Cliente(nombre_cl, apellido_cl, num_cuenta)
    num_cuenta += 1
    print(cliente_cl)
    return cliente_cl


def validacion(usuario):
    finalizar = False
    while finalizar == False:
        opcion = input(
            """1-Deposito
2-Retiro
3-Balance
4-Salir
Ingrese la opcion que desea realizar ingresando el numero:"""
        )
        if opcion == "1":
            print("LA OPCION ELEGIDA FUE DEPOSITAR")
            monto = int(input("Ingrese la cantidad que desea abonar: "))
            usuario.depositar(monto)
        elif opcion == "2":
            print("LA OPCION ELEGIDA FUE RETIRAR")
            monto = int(input("Ingrese la cantidad que desea retirar: "))
            usuario.retirar(monto)
        elif opcion == "3":
            print("LA OPCION ELEGIDA FUE MOSTRAR BALANCE")
            print(usuario)
        elif opcion == "4":
            print("EL programa ha finalizado")
            finalizar = True
        else:
            print("La opcion no es valida")


usuario = crear_cliente()
validacion(usuario)
