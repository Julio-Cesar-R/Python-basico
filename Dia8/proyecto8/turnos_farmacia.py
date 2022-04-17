from funciones_farmacia import generadores_decoradores
objeto_generadores=generadores_decoradores.decorar_saludo
salir=False

while salir==False:
    print('''Bienvenido a su farmacia
1-Perfumeria
2-Farmacia
3-Cosmeticos''')

    while True:
        try:
            opcion=int(input('''Seleccione con numeros el area para el 
cual desea obtener un turno: '''))
        except ValueError:
            print("LA OPCION INGRESADA NO FUE UN NUMERO\n")
        else:
            break


    if opcion in range(1,4):

        if opcion==1:
            objeto_generadores( opcion,"PERFUMERIA")
        elif opcion==2:
            objeto_generadores(opcion,"FARMACIA")
        elif opcion==3:
            objeto_generadores(opcion,"COSMETICOS")


    else:
        print("EL DEPARTAMENTO ELEGIDO NO EXISTE")



    while True:
        decision= input("Desea obtener otro turno? s/n: ")
        if decision== "n" or decision=="N":
            print("ADIOS VUELVA PRONTO\n")
            salir=True
            break

        elif decision== "s" or decision=="S":
            print("DE REGRESO AL MENU PRINCIPAL\n")
            break

        else:
            print("ESA NO ES UNA OPCION VALIDA\n")


