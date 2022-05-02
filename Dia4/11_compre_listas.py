palabra="juliorosas"
lista=[letra for letra in palabra]
print (lista)


lista=[letra for letra in "julio"]
print (lista)

lista=[num for num in range(1,31,2)if num*2>=10] # cracion de lista en ciclo con condicion
print (lista)

lista=[num if num*2>=10 else "no" for  num in range(1,31)] # cracion de lista en ciclo con condicion
print (lista)


lista=[10,20,30,40,50]
metros=[n*3.281 for n in lista]
print(metros)


metros=[n*3.281 for n in [10,20,30,40,50]]
print(metros)
#//////////////////////////////////////////////////////////////////////////
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado= [n**2 for n in valores]

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares=[n for n in valores if n%2==0 ]
print(valores_pares)

temperatura_fahrenheit = [32, 212, 275]
grados_celsius=[(n-32)*(5/9) for n in temperatura_fahrenheit]
