'''
Este programa sirve para hacer pruebas unitarias de una archivo.py
esta libreria ya la descargamos cuando instalamos python
'''
import unittest
import unittes_cambia_texto

class ProbarCambiaTexto(unittest.TestCase):#importa libreria
    def test_mayuscula(self):#siempre se define esta funcion como test_algo
        palabra="resultado en mayusculas"#este es el ejemplo que puse de prueba
        resultado=unittes_cambia_texto.todo_mayusculas(palabra)# el modulo,funcion y la prueba
        self.assertEqual(resultado,"Resultado En Mayusculas")#se hace la comparacion de lo que arroja el metodo con lo que se espera
if __name__ == "__main__":#Tu ponlo y ya
    unittest.main()

