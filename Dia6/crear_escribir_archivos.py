
archivo=open("prueba.txt",'w') # la "r"= lectura "w"=escritura' reemplaza todo "a"= escribe al dinal de un archivo creado
archivo.write("soy la nueva linea \n")#escribir dentro del archivo, no genera el salto de linea
archivo.write('''#soy la segunda nueva linea
esta es la tercera
la cuarta
la quinta
y asi
''')#las tres comillas simples son una mejor opcion para escribir un texto con saltos de linea
archivo.writelines(["hola ","mundo ","aqui ","estoy "])#ingresa una lista en una sola linea
archivo.close()


archivo=open("prueba.txt",'a')# no sobrescribe todo el texto agrega en la ultima linea
archivo.write(" escribio  hasta el final")
archivo.close()
#/////////////////////////////////////////////////////////////////////////////////
archivo=open("mi_archivo.txt",'w')
archivo.write("Nuevo texto")
archivo.close()
archivol=open("mi_archivo.txt",'r')
print(archivol.read())

archivo=open("mi_archivo.txt",'a')
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo=open("mi_archivo.txt",'r')
print(archivo.read())

archivo=open("registro.txt",'a')
registro_ultima_sesion = ["\nFederico\t", "20/12/2021\t", "08:17:32 hs\t", "Sin errores de carga\t"]
archivo.writelines(registro_ultima_sesion)
archivo.close()
archivo=open("registro.txt",'r')
print(archivo.read())