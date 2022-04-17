
def Perfumeria_generador():
    x = 1
    while True:
        yield f"P-{x}"
        x += 1
def Farmacia_generador():
    x = 1
    while True:
        yield f"F-{x}"
        x += 1
def Cosmeticos_generador():
    x = 1
    while True:
        yield f"C-{x}"
        x += 1

p=Perfumeria_generador()
f =Farmacia_generador()
c =Cosmeticos_generador()

def decorar_saludo(opcion,area):
    print("*"*30)
    print(f"\nUSTED HA ELEGIDO LA OPCION : {area}")
    if opcion==1:
         print(next(p))
    elif opcion==2:
        print(next(f))
    elif opcion==3:
        print(next(c))
    print("POR FAVOR ESPERE SU TURNO")
    print("*" * 30)