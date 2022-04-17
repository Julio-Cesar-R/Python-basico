def multiplica(num1,num2):
    '''
    Esta funcion sirve para multiplicar
    dos numeros cuales quiera
    '''
    return num1*num2
#n1=int(input("ingresa un numero"))
#n2=int(input("ingresa otro numero"))
datos=multiplica(19,15)
print((datos))

#//////////////////////////////////////////////////////////
def potencia(base,exponente):
    return base**exponente

dolares=49
def usd_a_eur(dolares):
    return dolares*0.85

palabra="algo"
def invertir_palabra(palabra):
    palabra=palabra[::-1].upper()
    return palabra
res=invertir_palabra(palabra)
print(res)